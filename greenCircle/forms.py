from django import forms
from greenCircle import models


class TrainerForm(forms.ModelForm):
    class Meta:
        model = models.Trainer
        fields = ['email', 'phone', 'image', 'address', 'last_name', 'first_name']
        widgets = {
            'email': forms.EmailInput(
                attrs={'id': 'email', 'class': 'form-control', 'placeholder': 'البريد الألكترونى '}),
            'phone': forms.TextInput(
                attrs={'id': 'phone', 'class': 'form-control', 'placeholder': 'الجوال '}),
            'image': forms.ClearableFileInput(),
            'address': forms.TextInput(
                attrs={'id': 'address', 'class': 'form-control', 'placeholder': 'العنوان '}),
            'last_name': forms.TextInput(
                attrs={'id': 'last_name', 'class': 'form-control', 'placeholder': 'اللقب '}),
            'first_name': forms.TextInput(
                attrs={'id': 'first_name', 'class': 'form-control', 'placeholder': 'الأسم '}),
        }
        labels = {
            'phone': 'الجوال',
            'first_name': 'الأسم',
            'last_name': 'اللقب',
            'email': 'البريد الألكترونى',
            'image': 'الصورة الشخصية',
            'address': 'العنوان',
        }


class CourseRequestForm(forms.ModelForm):
    class Meta:
        model = models.CourseRequest
        fields = ['email', 'phone', 'course', 'name']
        widgets = {
            'email': forms.EmailInput(
                attrs={'id': 'email', 'class': 'form-control', 'placeholder': 'البريد الألكترونى '}),
            'phone': forms.TextInput(
                attrs={'id': 'phone', 'class': 'form-control', 'placeholder': 'الجوال '}),
            'name': forms.TextInput(
                attrs={'id': 'name', 'class': 'form-control', 'placeholder': 'الأسم '}),
        }
        labels = {
            'phone': 'الجوال',
            'name': 'الأسم',
            'email': 'البريد الألكترونى',
        }
        exclude = ['course']


class GreenCourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ['name', 'trainer', 'logo', 'link', 'description', 'end_date', 'start_date', 'duration', 'category',
                  'total_hours']
        widgets = {
            'link': forms.URLInput(
                attrs={'id': 'link', 'class': 'form-control', 'placeholder': 'المسار الألكترونى '}),
            'duration': forms.NumberInput(
                attrs={'id': 'duration', 'class': 'form-control', 'placeholder': 'عدد الساعات '}),
            'total_hours': forms.NumberInput(
                attrs={'id': 'total_hours', 'class': 'form-control', 'placeholder': 'عدد ساعات الدائرة'}),
            'logo': forms.ClearableFileInput(),
            'description': forms.TextInput(
                attrs={'id': 'description', 'class': 'form-control', 'placeholder': 'المحتوى '}),
            'trainer': forms.Select(choices=models.Trainer.objects.all()),
            'category': forms.Select(choices=models.Category.objects.all()),
            'name': forms.TextInput(
                attrs={'id': 'name', 'class': 'form-control', 'placeholder': 'الأسم '}),
            'start_date': forms.TextInput(
                attrs={'id': 'start_date', 'type': 'date', 'class': 'form-control', 'placeholder': 'تاريخ البداية '}),
            'end_date': forms.TextInput(
                attrs={'id': 'end_date', 'type': 'date', 'class': 'form-control', 'placeholder': 'تاريخ النهاية '}),
        }
        labels = {
            'link': 'المسار الألكترونى ',
            'name': 'الأسم',
            'start_date': 'تاريخ البداية',
            'end_date': 'تاريخ النهاية',
            'logo': 'الشعار ',
            'trainer': 'المدرب',
            'category': 'التصنيف ',
            'description': 'المحتوى',
            'total_hours': 'عدد ساعات الدائرة ',
            'duration': 'عدد الساعات',
        }


class DocumentDownloadForm(forms.ModelForm):
    class Meta:
        model = models.DocumentDownload
        fields = ['name', 'email', 'phone', 'destination' , 'choice']
        widgets = {
            'email': forms.EmailInput(
                attrs={'id': 'email', 'class': 'form-control', 'placeholder': 'البريد الألكترونى '}),
            'phone': forms.TextInput(
                attrs={'id': 'phone', 'class': 'form-control', 'placeholder': 'الجوال '}),
            'name': forms.TextInput(
                attrs={'id': 'name', 'class': 'form-control', 'placeholder': 'الأسم '}),
            'destination': forms.Select(choices=models.DocumentDownload.DESTINATION_CHOICES),
            'choice': forms.Select(choices=models.DocumentDownload.DOWNLOAD_CHOICES)

        }
        labels = {
            'phone': 'الجوال',
            'name': 'الأسم',
            'email': 'البريد الألكترونى',
            'destination': 'الجهة',
            'choice': 'إختر الدليل'
        }
