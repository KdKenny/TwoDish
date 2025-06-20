from django import forms  # 添加缺少的import
from .models import comment_rate

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment_rate
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': '輸入您的評論...'})
        }
