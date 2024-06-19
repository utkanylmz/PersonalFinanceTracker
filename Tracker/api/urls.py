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
    # http://127.0.0.1:8000/api/incomes/
    path('incomes/<int:pk>/', IncomeDetailView.as_view(), name='income_detail'),
    # http://127.0.0.1:8000/api/incomes/
    
    
    path('expenses/', ExpenseListCreateView.as_view(), name='expense_list_create'),
    # http://127.0.0.1:8000/api/expenses/
    
    
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense_detail'),
    # http://127.0.0.1:8000/api/expenses/2/
   
    path('financial-summary/', FinancialSummaryView.as_view(), name='financial_summary'),
    # http://127.0.0.1:8000/api/financial-summary/
    
    path('expense-summary-by-date-range/', ExpenseSummaryByDateRangeView.as_view(), name='expense_summary_by_date_range'),
    # http://127.0.0.1:8000/api/expense-summary-by-date-range/?start_date=2024-01-01&end_date=2024-07-07
    
]