from django.db import models
from django.utils.translation import gettext_lazy as _

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
    desc = models.CharField(max_length=255, null=True, blank=True, verbose_name='التخصص')
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
    time = models.CharField(max_length=255, null=True, choices=TIME_CHOICES)
    place = models.CharField(max_length=255, null=True)
    study = models.CharField(max_length=255, null=True)
    skills = models.TextField(null=True)
    goals = models.TextField(null=True)
    filed = models.CharField(max_length=255, null=True)
    cv = models.FileField(null=True)
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
