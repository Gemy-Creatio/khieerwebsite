from django.db import models
from django.utils.translation import gettext_lazy as _
from django.templatetags.static import static
import os



class Volunteer(models.Model):
    email = models.EmailField(
        verbose_name=_('email address'), max_length=255, unique=True
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    address = models.CharField(_('Address'), max_length=255, null=True, blank=True)
    job = models.CharField(max_length=255, null=True, blank=True, verbose_name='المهنه')
    desc = models.TextField(max_length=255, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    GENDER_CHOICES = (
        ('ذكر', 'ذكر'),
        ('أنثى', 'انثى'),
    )
    gender = models.CharField(max_length=255, null=True, choices=GENDER_CHOICES)
    TIME_CHOICES = (
        ('متفرغ', 'متفرغ'),
        ('غير متفرغ', 'غير متفرغ'),
    )
    STUDY_CHOICES = (
        ('ثانوى' , 'ثانوى'),
        ('متوسط' , 'متوسط'),
        ('جامعى' , 'جامعى'),
        ('دراسات عليا' , 'دراسات عليا'),
    )
    FILED_CHOICES = (
        ('تصميم الجرافيك','تصميم الجرافيك'),
        ('محاسبة مالية','محاسبة مالية'),
        ('تصميم الموشن الجرافيك','تصميم الموشن الجرافيك'),
        ('كتابة المحتوى','كتابة المحتوى'),
        ('التصوير الفوتوغرافى','التصوير الفوتوغرافى'),
        ('التقنية','التقنية'),
        ('الأعمال المكتبية','الأعمال المكتبية'),
       ('التسويق الألكترونى','التسويق الألكترونى'),
       ('تصوير الفيديو ','تصوير الفيديو '),
       ('التدريب','التدريب'),
       ('التنظيم والتنسيق','التنظيم والتنسيق'),
       ('المونتاج تحرير الأفلام','المونتاج تحرير الأفلام'),
       ('التعليق الصوتى','التعليق الصوتى'),
        ('تسعير منتجات ','تسعير منتجات '),
       ('اخرى','اخرى'),
    )
    PLACE_CHOICES = (
        ('ميدانى','ميدانى'),
        ('عن بعد','عن بعد'),
        ('الأثنين معا','الأثنين معا'),
    )
    time = models.CharField(max_length=255, null=True, choices=TIME_CHOICES)
    place = models.CharField(max_length=255, null=True ,choices=PLACE_CHOICES)
    study = models.CharField(max_length=255, null=True , choices=STUDY_CHOICES)
    skills = models.TextField(null=True)
    goals = models.TextField(null=True)
    filed = models.CharField(max_length=255, null=True ,choices=FILED_CHOICES)
    cv = models.FileField(upload_to='joiners_cv/',null=True,blank=True)
    @property
    def cv_url(self):
        if self.cv and hasattr(self.cv, 'url'):
            if os.path.isfile(self.cv.url):
                return self.cv.url
            else:
                return None
        else:
            return None

    date_received = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class HebaKheer(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='اسم ')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='العنوان')
    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='الهاتف')
    ammount = models.IntegerField(null=True, blank=True, verbose_name='المبلغ')

    def __str__(self):
        return self.name
