from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '用戶名...',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '密碼...'
    }))