from django.contrib import admin, messages

from apps.balance.models import BillEntry, Bill, BillTransaction, AccountBillTransaction
from apps.balance.services.service import TransactionLogic


class BillEntryAdmin(admin.TabularInline):
    model = BillEntry
    extra = 0
    max_num = 100
    readonly_fields = ('bill', 'transaction')
    ordering = ("-id",)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'balance',
                    'created_at', 'modified_at',)
    list_display_links = ('id', 'user',)
    # readonly_fields = ('user', 'balance')
    search_fields = (
        'user__username',
        'user__email',
        'id',
        'created_at',
    )
    list_filter = (
        'created_at',
        'modified_at',
    )
    inlines = [BillEntryAdmin]


class AccountBillTransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'to_bill', 'amount', 'reason',
                    'created_at')
    list_display_links = ('id', 'amount')
    readonly_fields = ('created_at', 'reason')
    # raw_id_fields = ('from_account', 'to_account')
    list_filter = (
        'created_at',
    )
    filter_horizontal = ("from_bills",)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        """
        Фильтр вывода счетов для показа

        Для счетов from_bill - показываем только свои счета
        """
        if db_field.name == "from_bills":
            kwargs["queryset"] = Bill.objects.filter(user=request.user)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Фильтр вывода счетов для показа
        Для счетов to_bill - не показываем свои счета.
        """
        if db_field.name == "to_bill":
            kwargs["queryset"] = Bill.objects.exclude(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_related(self, request, form, formsets, change):
        """Разделение перевода по счетам и оповещение сообщением об операции"""
        super(AccountBillTransactionAdmin, self).save_related(request, form, formsets, change)

        # TODO: перетащить всю логику в класс TransactionLogic, если будет одинаковый код и в других местах
        trans_process = TransactionLogic(form.instance)
        can_transaction, msg = trans_process.can_do_transaction()
        if can_transaction:
            # проводим транзакцию
            result, msg = trans_process.do_transaction()
            # меняем статус
            trans_process.billed_transaction()
            return messages.add_message(request, messages.INFO, msg)
        # отмена транзакции
        trans_process.cancel_transaction()
        messages.add_message(request, messages.WARNING, msg)

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class BillTransactionAdmin(admin.ModelAdmin):
    list_display = ('id', "to_bill", "amount", "reason",
                    'created_at')
    list_display_links = ('id', "amount")
    readonly_fields = ('created_at',)
    # raw_id_fields = ('from_account', 'to_account')
    list_filter = (
        'created_at',
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Фильтр вывода счетов для показа
        Для счетов to_bill - не показываем свои счета.
        Для счетов from_bill - показываем только свои счета
        """

        if db_field.name == "to_bill":
            kwargs["queryset"] = Bill.objects.exclude(user=request.user)
        if db_field.name == "from_bill":
            kwargs["queryset"] = Bill.objects.filter(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        """BillTransaction только для просмотра. Все транзакции проходят через AccountBillTransaction"""
        return False


admin.site.register(Bill, BillAdmin)
admin.site.register(BillTransaction, BillTransactionAdmin)
admin.site.register(AccountBillTransaction, AccountBillTransactionAdmin)
