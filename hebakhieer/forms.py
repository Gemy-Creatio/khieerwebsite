
from django import forms
from . import models




class VolunteerForm(forms.ModelForm):
    class Meta:
        model = models.Volunteer
        fields = '__all__'
        exclude = ('date_received',)
        widgets = {
               'birthdate': forms.TextInput(
                attrs={'id': 'birthdate', 'type': 'date', 'class': 'form-control', 'placeholder': 'تاريخ الميلاد '}),
        }
        labels = {
            'first_name': 'الاسم الاول',
            'last_name': 'الاسم الثاني',
            'email': 'البريد الألكترونى',
            'job': 'الوظيفة',
            'phone': 'رقم الجوال',
            'address': 'العنوان',
            'birthdate': 'تاريخ الميلاد',
             'cv':'السيرة الذاتية',
             'goals':'الهدف من التطوع',
             'skills':'المهارات',
             'desc':'نبذه عن المتطوع',
             'gender':'النوع',
             'time':'التفرغ',
             'study':'المؤهل الدراسى',
             'filed':'المجال الذى ترغب التطوع به',
             'place':'موقع التطوع',
        }