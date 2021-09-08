from django.db import models


class TechnicalSupport(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='الأسم')
    message = models.TextField(blank=True, null=True, verbose_name='الرساله')

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='الأسم')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='العنوان')
    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='الهاتف')
    message = models.TextField(null=True, blank=True, verbose_name='الرساله')

    def __str__(self):
        return self.name


class FAQ(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Blogs(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    video_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
