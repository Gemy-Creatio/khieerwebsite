from django.contrib import admin

from . import models

admin.site.register(models.TechnicalSupport)
admin.site.register(models.Contact)
admin.site.register(models.Blogs)
admin.site.register(models.FAQ)

