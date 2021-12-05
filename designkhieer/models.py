from django.db import models

# Create your models here.
class KhieerDesign(models.Model):
    name = models.CharField(max_length=255 , null=True , blank=True)
    image =  models.ImageField(upload_to='designs/', null=True)
    def __str__(self) -> str:
        return self.name