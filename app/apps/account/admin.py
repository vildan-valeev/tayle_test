from django.contrib import admin

from apps.account.models import Account
from apps.balance.models import Bill


class BillAdmin(admin.TabularInline):
    model = Bill
    extra = 0
    max_num = 100
    readonly_fields = ('balance', 'user')
    ordering = ("-id",)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class AccountAdmin(admin.ModelAdmin):
    # вывод полей в списке записей в админке
    list_display = ('id', 'username')
    inlines = [BillAdmin]


admin.site.register(Account, AccountAdmin)
