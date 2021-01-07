from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from bootstrap_datepicker_plus import DatePickerInput

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', )

class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'date_of_birth', 'location' ]
        widgets = {'date_of_birth': DatePickerInput()}

        