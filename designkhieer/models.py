from django.db import models


# Create your models here.
class KhieerDesign(models.Model):
    image = models.ImageField(upload_to='designs/', null=True)

    def __str__(self) -> str:
        return self.name


class DesignRequest(models.Model):
    product = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    type_clothes = models.CharField(max_length=100, null=True, blank=True)
    number_of_order = models.SmallIntegerField(max_length=255, blank=True)
    design_image = models.ForeignKey(KhieerDesign, null=True, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def Price(self):
        return self.number_of_order * 30


class DesignerJoinUs(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    national_id = models.CharField(max_length=255, null=True, blank=True)
    signature = models.CharField(max_length=255, null=True, blank=True)
    design_filed = models.CharField(max_length=255, null=True, blank=True)
    is_accept_policy = models.BooleanField(null=True, blank=True, default=False)
    @property
    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
