from django.contrib import admin

from apps.balance.models import BillEntry, Bill, BillTransaction, AccountBillTransaction


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
    list_display = ('id', "to_bill", "amount", "reason",
                    'created_at')
    list_display_links = ('id', "amount")
    readonly_fields = ('created_at',)
    # raw_id_fields = ('from_account', 'to_account')
    list_filter = (
        'created_at',
    )
    filter_horizontal = ("from_bills",)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "from_bills":
            kwargs["queryset"] = Bill.objects.filter(user=request.user)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "to_bill":
            kwargs["queryset"] = Bill.objects.exclude(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

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
        if db_field.name == "to_bill":
            kwargs["queryset"] = Bill.objects.exclude(user=request.user)
        if db_field.name == "from_bill":
            kwargs["queryset"] = Bill.objects.filter(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Bill, BillAdmin)
admin.site.register(BillTransaction, BillTransactionAdmin)
admin.site.register(AccountBillTransaction, AccountBillTransactionAdmin)
