'''自定义form'''
from django import forms

class PostAdminForm(forms.ModelForm):
    '''定义摘要展示方式'''
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
