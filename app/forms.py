from django import forms
from .models import Accounts
from django_recaptcha.fields import ReCaptchaField

class AccountCreationForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = "__all__"
        exclude = ['balance','pin']


class Recaptcha(forms.Form):
    recaptcha = ReCaptchaField()