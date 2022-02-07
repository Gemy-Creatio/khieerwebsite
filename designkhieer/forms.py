from django import forms
from . import models


class KhieerDesignForm(forms.ModelForm):
    image = forms.ImageField(label=' الصورة')

    class Meta:
        model = models.KhieerDesign
        fields = '__all__'
        labels = {
            'image': 'الصورة',
        }
