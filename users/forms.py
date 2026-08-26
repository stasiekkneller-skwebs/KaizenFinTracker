from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User 

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None

        self.fields['username'].label = 'Nazwa użytkownika'
        self.fields['email'].label = 'Adres email'
        self.fields['password1'].label = 'Hasło'
        self.fields['password2'].label = 'Powtórz hasło'

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nazwa użytkownika'
        self.fields['password'].label = 'Hasło'

