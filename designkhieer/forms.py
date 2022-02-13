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


class DesignerJoinUsForm(forms.ModelForm):
    class Meta:
        model = models.DesignerJoinUs
        fields = '__all__'
        exclude = ('is_accept_policy',)
        labels = {
            'first_name': 'الاسم الاول',
            'last_name': 'الاسم الثاني',
            'email': 'البريد الألكترونى',
            'national_id': 'رقم الهوية/ رقم الاقامة',
            'phone': 'رقم الجوال',
            'signature': 'المقر',
            'design_filed': 'مجال التصميم',
        }
