from django.db.models import Sum
from Tracker.models import Income, Expense

def total_income(user):
    return user.incomes.aggregate(Sum('amount'))['amount__sum'] or 0

def total_expense(user):
    return user.expenses.aggregate(Sum('amount'))['amount__sum'] or 0

def current_balance(user):
    return total_income(user) - total_expense(user)

def get_income_by_category(user):
    return user.incomes.values('source').annotate(total=Sum('amount'))

def get_expense_by_category(user):
    return user.expenses.values('category').annotate(total=Sum('amount'))

def expenses_by_date_range(user, start_date, end_date):
    return user.expenses.filter(date__range=[start_date, end_date]).values('category').annotate(total=Sum('amount'))
