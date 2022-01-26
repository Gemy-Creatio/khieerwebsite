from django.contrib import admin
from . import models


admin.site.register(models.Category)
admin.site.register(models.CourseRequest)
admin.site.register(models.Trainer)
admin.site.register(models.Course)
admin.site.register(models.DocumentDownload)
admin.site.register(models.GreenSurvey)