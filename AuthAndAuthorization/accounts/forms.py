from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

UserModel = get_user_model()

class SetUnusablePasswordForm(forms.Form):
    user = forms.ModelChoiceField(
        queryset=UserModel.objects.order_by('username'),
    )

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data["user"].is_superuser:
            raise ValidationError("Cannot ban the superuser")

        return cleaned_data