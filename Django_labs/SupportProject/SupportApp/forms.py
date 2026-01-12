from django import forms
from django.core.exceptions import ValidationError

CATEGORY_CHOICES = [
    ('login', 'Login problem'),
    ('payment', 'Payment'),
    ('bug', 'Bug report'),
    ('other', 'Other'),
]

class SupportTicketForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False)

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 20:
            raise ValidationError("Message must be at least 20 characters long.")
        return message

    def clean_full_name(self):
        name = self.cleaned_data.get('full_name')
        if len(name.split()) < 2:
            raise ValidationError("Please enter first and last name.")
        return name
