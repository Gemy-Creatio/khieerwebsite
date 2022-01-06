from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _


class Trainer(models.Model):
    image = models.ImageField(verbose_name='Image', null=True)
    email = models.EmailField(
        verbose_name=_('email address'), max_length=255, unique=True
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    address = models.CharField(_('Address'), max_length=255, null=True, blank=True)

    @property
    def FullName(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.first_name


class Category(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='اسم التصنيف')
    description = models.CharField(max_length=255, null=True, verbose_name='عن التصنيف')

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='اسم الدوره')
    description = models.CharField(max_length=255, null=True, verbose_name='عن الدوره')
    logo = models.ImageField(verbose_name='لوجو الدوره', null=True)
    duration = models.SmallIntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='التصنيف')
    link = models.URLField(
        verbose_name='المسار',
        max_length=128,
        db_index=True,
        unique=True,
        blank=True,
        null=True
    )
    start_date = models.DateField(verbose_name="تاريخ البدايه", null=True, auto_now=False, auto_now_add=False)
    end_date = models.DateField(verbose_name="تاريخ النهايه", null=True, auto_now=False, auto_now_add=False, )
    total_hours = models.IntegerField(null=True, blank=True, verbose_name='عدد الساعات')
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='courses', verbose_name='المدرب')

    @property
    def is_past_due(self):
        return date.today() > self.end_date

    def __str__(self):
        return self.name


class CourseRequest(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='اسم الملتحق')
    email = models.EmailField(
        verbose_name=_('email address'), max_length=255
    )
    phone = models.CharField(max_length=255, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name='Requests')

    def __str__(self):
        return self.name


class DocumentDownload(models.Model):
    DESTINATION_CHOICES = (
        (1, 'افراد'),
        (2, 'قطاع عام'),
        (3, 'قطاع خاص'),
        (4, 'قطاع غير ربحى'),
    )
    name = models.CharField(null=True, blank=True, max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(null=True, blank=True , max_length=255)
    destination = models.SmallIntegerField(null=True, choices=DESTINATION_CHOICES)

    def __str__(self):
        return self.name
