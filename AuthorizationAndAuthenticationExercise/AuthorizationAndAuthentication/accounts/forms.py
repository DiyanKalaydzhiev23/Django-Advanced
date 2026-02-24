from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

UserModel = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email')


class SetUnusablePasswordForm(forms.Form):
    user = forms.ModelChoiceField(
        queryset=UserModel.objects.order_by('username'),
        label="User",
    )
