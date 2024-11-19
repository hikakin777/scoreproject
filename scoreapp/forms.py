# forms.py
from django import forms
from .models import ScorePost, Category 


class ScorePostForm(forms.ModelForm):  
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="選択してください")

    class Meta:
        model = ScorePost
        fields = ['category', 'title','price','condition','day']  
    
    
