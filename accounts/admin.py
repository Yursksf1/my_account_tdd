from django.contrib import admin
from accounts.models import account, transactionCategory, transaction 

class AccountAdmin(admin.ModelAdmin):
	list_display = ('id','name', 'owner', 'description')

admin.site.register(account, AccountAdmin)


class TransactionCategoryAdmin(admin.ModelAdmin):
	list_display = ('id','name', 'description', 'income')

admin.site.register(transactionCategory, TransactionCategoryAdmin)


class TransactionAdmin(admin.ModelAdmin):
	list_display = ('id','value', 'category', 'description', 'account', 'date')

admin.site.register(transaction, TransactionAdmin)


