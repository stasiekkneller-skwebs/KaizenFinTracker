from django.urls import path
from .views import DashboardView, AddCategoryView, CategoryListView, CategoryUpdateView, CategoryDetailView, CategoryDeleteView, AddTransactionView, TransactionListView, TransactionDeleteView, TransactionDetailView, HomeView, TransactionUpdateView, UploadFileView, AddBudgetView, UpdateBudgetView, BudgetListView, BudgetDeleteView, ExportTransactionsView
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('add-category/', AddCategoryView.as_view(), name="add-category"),
    path('add-transaction/', AddTransactionView.as_view(), name="add-transaction"),
    path('categories/', CategoryListView.as_view(), name="all-categories"),
    path('transactions/', TransactionListView.as_view(), name="all-transactions"),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name="update-category"),
    path('transactions/update/<int:pk>/', TransactionUpdateView.as_view(), name="update-transaction"),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name="category-details"),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name="transaction-details"),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name="delete-category"),
    path('transactions/delete/<int:pk>/', TransactionDeleteView.as_view(), name="delete-transaction"),
    path('transactions/upload/', UploadFileView.as_view(), name="upload-transactions"),
    path('budgets/set/', AddBudgetView.as_view(), name="add-budget"),
    path('budgets/update/<int:pk>/', UpdateBudgetView.as_view(), name="update-budget"),
    path('budgets/', BudgetListView.as_view(), name="all-budgets"),
    path('budgets/delete/<int:pk>/', BudgetDeleteView.as_view(), name="delete-budget"),
    path('transactions/export/', ExportTransactionsView.as_view(), name='transactions_export'),
]