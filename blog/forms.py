from django import forms

class SubscribeForm(forms.Form):
    email = forms.EmailField(help_text='Subscribe to our blog')