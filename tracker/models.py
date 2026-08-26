import uuid
import os
from django.db import models
from django.conf import settings
from django.utils import timezone
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

ACCOUNT_CHOICES = [
    ('cash', 'Gotówkowe'),
    ('main', 'Główne'),
    ('currency', 'Walutowe'),
]

TYPE_CHOICES = [
        ('expense', 'Wydatek'),
        ('income', 'Przychód'),
    ]

FREQUENCY_CHOICES = [
    ('weekly', 'Co tydzień'),
    ('monthly', 'Co miesiąc'),
]

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name


def user_receipt_directory_path(instance, filename):
    # Wyciągamy rozszerzenie pliku (np. .jpg, .png)
    ext = filename.split('.')[-1]
    # Generujemy unikalną nazwę pliku za pomocą UUID transakcji
    filename = f"{instance.transaction_id}.{ext}"
    # Zwraca ścieżkę: media/receipts/user_<id>/<rok>/<miesiac>/<filename>
    return os.path.join(
        'receipts', 
        f'user_{instance.user.id}', 
        instance.transaction_date.strftime('%Y'), 
        instance.transaction_date.strftime('%m'), 
        filename
    )




    
class Budget(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    category  = models.ForeignKey(Category,null=True, blank=True, on_delete=models.SET_NULL)
    limit = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    month = models.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)]  , default=timezone.now().month)
    year = models.IntegerField(default=timezone.now().year)
    class Meta:
        unique_together = ['user', 'category', 'month', 'year']

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    balance = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_CHOICES)
    color = models.CharField(max_length=7)

    #transakcje



class EmailReport(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    is_active = models.BooleanField(default=False)
    last_sent = models.DateTimeField(null=True)

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name =models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category,null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    description = models.CharField(max_length=255, blank=True)
    receipt_image = models.ImageField(
        upload_to=user_receipt_directory_path, # wskazujemy na naszą funkcję
        null=True,
        blank=True
    )
    transaction_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(
    Account,
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='transactions'
    )
    

    class Meta:
        ordering = ['-transaction_date']

    def display_amount(self):
        if self.transaction_type == 'expense':
            return f"-{self.amount}"
        return f"{self.amount}"
    
    def __str__(self):
        return f"{self.transaction_type} — {self.amount} zł ({self.transaction_date})"