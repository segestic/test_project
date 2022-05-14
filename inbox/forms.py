from django import forms
from .models import Mail


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = [
            "subject",
            "content",
        ]
        

class SendMailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = [
            "user",
            "subject",
            "content",
        ]
                