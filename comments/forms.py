from django import forms
from .models import comment_rate

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment_rate
        fields = ['comment']
