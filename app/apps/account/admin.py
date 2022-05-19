from django.contrib import admin

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    # вывод полей в списке записей в админке
    list_display = ('id', 'first_name')


admin.site.register(Account, AccountAdmin)
