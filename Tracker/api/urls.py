from django.urls import path
from Tracker.api.views import (
    IncomeListCreateView,
    IncomeDetailView,
    ExpenseListCreateView,
    ExpenseDetailView,
    FinancialSummaryView,
    ExpenseSummaryByDateRangeView
)

urlpatterns = [
    path('incomes/', IncomeListCreateView.as_view(), name='income_list_create'),
    path('incomes/<int:pk>/', IncomeDetailView.as_view(), name='income_detail'),
    path('expenses/', ExpenseListCreateView.as_view(), name='expense_list_create'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense_detail'),
    path('financial-summary/', FinancialSummaryView.as_view(), name='financial_summary'),
    path('expense-summary-by-date-range/', ExpenseSummaryByDateRangeView.as_view(), name='expense_summary_by_date_range'),
]