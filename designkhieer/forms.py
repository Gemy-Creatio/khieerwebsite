from django import forms
from . import models

class KhieerDesignForm (forms.ModelForm):
    image = forms.ImageField(label=' الصورة')
    class Meta:
        model = models.KhieerDesign
        fields = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs={'id': 'residentRatefield', 'class': 'form-control', 'placeholder': 'العنوان '}),
           
          }
        labels = {
            'name': 'العنوان',
        }
