from django import forms


class VerifyForm(forms.Form):
    type = forms.CharField(label="Evento", initial="", required=False)