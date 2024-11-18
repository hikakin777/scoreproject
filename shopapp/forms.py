# forms.py
from django import forms
from .models import ShopPost, Category 


class ShopPostForm(forms.ModelForm):  
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="選択してください")

    class Meta:
        model = ShopPost
        fields = ['category', 'title','price','condition','day']  
    
    
