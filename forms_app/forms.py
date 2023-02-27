from django import forms

class FormContatto(forms.Form):
    nome = forms.CharField()
    cognome = forms.CharField()
    email = forms.CharField()
    contenuto = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Area testuale scrivi pure!"}))