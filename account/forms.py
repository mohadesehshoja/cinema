import form
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ValidationError
import string
from account.models import Payment, profile


class Payment_Form(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'transaction_id']

    def clean(self):
        super().clean()
        id = self.cleaned_data.get("transaction_id")
        amount = self.cleaned_data.get("amount")
        if amount is not None and id is not None:
            if int(amount) != int(id.split("_")[1]):
                raise ValidationError("the amount dosnt match transaction id")

    def clean_amount(self):
        amount = self.cleaned_data.get("amount")
        if int(amount) < 1000:
            raise ValidationError("its less than 1000")
        return amount

    def clean_transaction_id(self):
        id = self.cleaned_data.get("transaction_id")
        try:
            assert id.startswith("bank_")
            assert id.endswith("#")
            parts = id.split("_")
            assert len(parts) == 3
            int(parts[1])
        except:
            raise ValidationError("the format isnt valid")
        return id


class Profile_Form(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['mobile', 'gender', 'address', 'profileimage']


class myuser_form(forms.ModelForm):
    class Meta(UserChangeForm.Meta):
        fields = ['first_name', "last_name", "email"]
    password = None


class ChangePassword(forms.Form):
    new_password = forms.PasswordInput()
