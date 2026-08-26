from django import forms
from .models import Category, Transaction, Budget

class CategoryCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'color']
        widgets ={
            'color': forms.ColorInput()
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None

        self.fields['name'].label = 'Nazwa kategorii'
        self.fields['color'].label = 'Kolor tagu'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Category.objects.filter(user=self.user, name=name).exists():
            raise forms.ValidationError('Kategoria o tej nazwie już istnieje.')
        return name

class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'color']
        widgets ={
            'color': forms.ColorInput()
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None

        self.fields['name'].label = 'Nazwa kategorii'
        self.fields['color'].label = 'Kolor tagu'



from django import forms
from .models import Transaction, Category

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['name', 'category', 'amount', 'transaction_type', 'description', 'transaction_date', 'receipt_image']
        # Dopisujemy widżet dla pola transaction_date
        widgets = {
            'transaction_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['category'].queryset = Category.objects.filter(user=self.user)
        for field in self.fields.values():
            field.help_text = None

        self.fields['name'].label = 'Nazwa transakcji'
        self.fields['category'].label = 'Nazwa kategorii'
        self.fields['amount'].label = 'Kwota'
        self.fields['transaction_type'].label = 'Typ transakcji'
        self.fields['description'].label = 'Opis transakcji'
        self.fields['transaction_date'].label = 'Data transakcji'


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['category', 'limit', 'month', 'year']
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['category'].queryset = Category.objects.filter(user=self.user)
        for field in self.fields.values():
            field.help_text = None

        self.fields['category'].label = 'Nazwa kategorii'
        self.fields['limit'].label = 'Limit kwoty'
        self.fields['month'].label = 'Miesiąc'
        self.fields['year'].label = 'Rok'
    
    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        month = cleaned_data.get('month')
        year = cleaned_data.get('year')

        if category and month and year:
            exists = Budget.objects.filter(
                user=self.user,
                category=category,
                month=month,
                year=year
            ).exists()
            if exists:
                raise forms.ValidationError(
                    f'Budżet dla kategorii "{category}" w {month}/{year} już istnieje.'
                )
        return cleaned_data
    
class BudgetUpdateForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['category', 'month', 'year', 'limit']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['category'].queryset = Category.objects.filter(user=self.user)
        for field in self.fields.values():
            field.help_text = None

        self.fields['category'].label = 'Nazwa kategorii'
        self.fields['limit'].label = 'Limit kwoty'
        self.fields['month'].label = 'Miesiąc'
        self.fields['year'].label = 'Rok'

        self.fields['category'].disabled = True
        self.fields['month'].disabled = True
        self.fields['year'].disabled = True
    
    

