from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from Tracker.models import Income, Expense
from Tracker.api.serializers import IncomeSerializer, ExpenseSerializer
from Tracker.api.services import (
    total_income,
    total_expense,
    current_balance,
    get_income_by_category,
    get_expense_by_category,
    expenses_by_date_range
)

# Income CRUD operations
class IncomeListCreateView(generics.ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class IncomeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)

# Expense CRUD operations
class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

# Financial summary operations
class FinancialSummaryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        data = {
            'total_income': total_income(user),
            'total_expense': total_expense(user),
            'current_balance': current_balance(user),
            'income_by_category': list(get_income_by_category(user)),
            'expense_by_category': list(get_expense_by_category(user)),
        }
        return Response(data)

class ExpenseSummaryByDateRangeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        data = expenses_by_date_range(user, start_date, end_date)
        return Response(data)
