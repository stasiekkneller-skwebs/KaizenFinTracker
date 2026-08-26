from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Budget, Account, EmailReport, Transaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'user')
    list_filter = ('user',)
    search_fields = ('name',)


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'limit', 'month', 'year')
    list_filter = ('year', 'month', 'category')
    search_fields = ('user__username', 'category__name')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'account_type', 'balance', 'color')
    list_filter = ('account_type',)
    search_fields = ('name', 'user__username')


@admin.register(EmailReport)
class EmailReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'frequency', 'is_active', 'last_sent')
    list_filter = ('frequency', 'is_active')
    search_fields = ('user__username',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'transaction_id', 'user', 'name', 'category', 'amount',
        'transaction_type', 'transaction_date', 'account',
    )
    list_filter = ('transaction_type', 'category', 'account', 'transaction_date')
    search_fields = ('name', 'description', 'user__username')
    date_hierarchy = 'transaction_date'
    readonly_fields = ('transaction_id', 'created_at')