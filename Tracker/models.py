from django.db import models
from django.contrib.auth.models import User

class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=255)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incomes')

    def __str__(self):
        return f"{self.source} - {self.amount}"
    
    
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('FOOD', 'Food'),
        ('TRANSPORT', 'Transport'),
        ('ENTERTAINMENT', 'Entertainment'),
        ('UTILITIES', 'Utilities'),
        ('OTHER', 'Other'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')

    def __str__(self):
        return f"{self.category} - {self.amount}"
    
class Budget(models.Model):
    category = models.CharField(max_length=50, choices=Expense.CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')

    def __str__(self):
        return f"{self.category} - {self.amount} for {self.month}"