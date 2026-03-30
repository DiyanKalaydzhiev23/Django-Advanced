from django import forms
from advertisement_center.models import Commercial


class CommercialForm(forms.ModelForm):
    class Meta:
        model = Commercial
        fields = ['slogan', 'body', 'video']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 6}),
            'slogan': forms.TextInput(attrs={'placeholder': 'Short punchy slogan'}),
        }
