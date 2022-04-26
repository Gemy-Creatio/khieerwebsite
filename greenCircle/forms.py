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
            'destination_name': "إسم الجهة"
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



class FinishCircleForm(forms.ModelForm):
    class Meta:
        model = models.FinishCircle
        fields = '__all__'
        labels = {
            'is_loved':'هل تريد تصبح هذه القضية شغفك ؟',
            'help_accepted': 'هل تمت المساعدة؟ ',
            'notes':'اكتب مرئياتك وملاحظاتك',
            'is_entertainment':'هل استمتعت في هذه الرحلة',
        }

class DocumentDownloadForm(forms.ModelForm):
    class Meta:
        model = models.DocumentDownload
        fields = '__all__'
        exclude = ('user' , )
        labels = {
            'firstName': ' الأسم الأول',
            'lastName': ' الأسم الثانى',
            'phone': 'الجوال',
            'email': 'البريد الألكترونى',
            'destination': 'الجهة',
            'destination_name': "إسم الجهة",
            'choice': 'إختر الدليل',
            'category':'إختر المسار'
        }


class GreenSurveyForm(forms.ModelForm):
    class Meta:
        model = models.GreenSurvey
        fields = ['is_accepted', 'choices']
        widgets = {
            'choices': forms.Select(choices=models.GreenSurvey.GREEN_CHOICES),
            'is_accepted': forms.Select(choices=models.GreenSurvey.ACCEPTED_CHOICES),

        }
        labels = {
            'is_accepted': ' هل تريد ان تكون قضيتك وشغفك',
            'choices': 'نوع القضية'
        }



class TopicSurveyForm(forms.ModelForm):
    class Meta:
        model = models.TopicSurvery
        fields = '__all__'
        exclude = ['user', ]
        labels = {
            'help_way': ' كيف يمكننا مساعدة الحرفية مسعودة على إنتاج القطع بكميات كبيرة وفي فترات زمنية قصيرة؟',
            'provide_help': 'هل تود أن تساند الحرفية مسعودة بتوفير الخيوط لها والأدوات لتنتج؟ ',
            'women_support':'هل تود دعم مجتمع السيدات الحرفيات بحرفة الخيوط في القرية؟',
       }

class VolunteerTripForm(forms.ModelForm):
    class Meta:
        model = models.VolunteerTrip
        fields = '__all__'
        labels = {
            'first_name': 'الأسم الأول',
            'last_name': 'إسم العائلة',
            'phone': 'رقم التواصل',
            'email': 'البريد الألكترونى',
            'national_id_type': 'نوع الهوية',
            'national_id_number': 'رقم الهوية',
            'age': 'الفئة العمرية',
            'why_you_join': 'لماذا تريد الأنضمام إلى الرحالات التنموية التطوعية؟',
            'accept_pay': 'أوافق على دفع نصف تكاليف الرحلة',

        }
