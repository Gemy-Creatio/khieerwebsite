from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import(
    User
)

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

class TopicSurvery(models.Model):
    QUESTION_ANSWERS = (
        (True, 'نعم'),
       (False, 'لا'),
    )
    help_way = models.TextField(null=True , blank=True)
    provide_help = models.BooleanField(null=True , blank=True ,choices=QUESTION_ANSWERS )
    women_support = models.BooleanField(null=True , blank=True ,choices=QUESTION_ANSWERS )
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    def __str__(self) -> str:
        return self.user.first_name

class DocumentDownload(models.Model):
    GREEN = '2_GREEN'
    DESTINATION_CHOICES = (
        (1, 'افراد'),
        (2, 'قطاع عام'),
        (3, 'قطاع خاص'),
        (4, 'قطاع غير ربحى'),
    )
    DOWNLOAD_CHOICES = (
        (GREEN, 'تكوين دائرة'),

    )
    CATEGORY_CHOICES = (
        ('مسار الوعى' , 'مسار الوعى'),
        ('مسار الأرشاد' , 'مسار الأرشاد'),
        ('مسار الولاء ' , 'مسار الولاء '),
        (' لا ارغب  ' , ' لا ارغب '),
    )
    choice = models.CharField(max_length=255, null=True, blank=True, choices=DOWNLOAD_CHOICES)
    firstName = models.CharField(null=True, blank=True, max_length=255)
    lastName = models.CharField(null=True, blank=True, max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(null=True, blank=True, max_length=255)
    destination = models.SmallIntegerField(null=True, choices=DESTINATION_CHOICES)
    destination_name = models.CharField(null=True, blank=True, max_length=255)
    user = models.ForeignKey(User , null=True , blank=True , on_delete=models.CASCADE)
    category = models.CharField(null=True, blank=True, max_length=255 , choices=CATEGORY_CHOICES)
    def __str__(self):
        return self.firstName


class GreenSurvey(models.Model):
    document_download = models.ForeignKey(DocumentDownload, null=True, on_delete=models.CASCADE,
                                          related_name='green_survey')
    ACCEPTED_CHOICES = (
        (True, 'نعم'),
        (False, 'لا'),
    )
    is_accepted = models.BooleanField(null=True, blank=True, choices=ACCEPTED_CHOICES)
    SOCIATY_SUPPORT = 'الاطفال المحتضنين '
    TEXT_SUPPORT = 'دعم حرفة الخيوط '
    GREEN_CHOICES = (
        (SOCIATY_SUPPORT, SOCIATY_SUPPORT),
        (TEXT_SUPPORT, TEXT_SUPPORT),

    )

    choices = models.CharField(max_length=255, choices=GREEN_CHOICES)

    def __str__(self):
        return self.choices



class FinishCircle(models.Model):
    ACCEPTED_CHOICES = (
        (True, 'نعم'),
        (False, 'لا'),
    )
    help_accepted = models.BooleanField(null=True, blank=True, choices=ACCEPTED_CHOICES)
    notes = models.TextField(max_length=255,null=True , blank=True)
    is_entertainment =  models.BooleanField(null=True, blank=True, choices=ACCEPTED_CHOICES)
    is_loved =  models.BooleanField(null=True, blank=True, choices=ACCEPTED_CHOICES)
    def __str__(self) -> str:
        return self.notes
    




class VolunteerTrip(models.Model):
    ID_CHOICES = (
        ('إقامة', 'إقامة'),
        ('هوية وطنية', 'هوية وطنية')
    )

    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    national_id_type = models.CharField(max_length=100, null=True, choices=ID_CHOICES)
    national_id_number = models.IntegerField(null=True, blank=True)
    age = models.SmallIntegerField(null=True, blank=True)
    why_you_join = models.TextField(null=True, blank=True)


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name



class GreenTopic(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='التصنيف')
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    joiners = models.ManyToManyField(User , null=True , blank=True )
    
    def __str__(self):
        return self.name
    



class Messgaes (models.Model):
    sent_to = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    content = models.TextField(null=True , blank=True)
    file = models.FileField(upload_to='messages/' , null=True , blank=True)
    link = models.URLField(null=True , blank=True)
    timeStamp = models.DateField(auto_now_add=True , blank=True ,null=True)
    def __str__(self):
        return self.content
