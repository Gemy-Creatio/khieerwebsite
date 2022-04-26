from django.contrib import admin
from . import models


admin.site.register(models.Category)
admin.site.register(models.CourseRequest)
admin.site.register(models.Trainer)
admin.site.register(models.Course)
admin.site.register(models.DocumentDownload)
admin.site.register(models.GreenSurvey)

admin.site.register(models.GreenTopic)
admin.site.register(models.TopicSurvery)
admin.site.register(models.FinishCircle)
