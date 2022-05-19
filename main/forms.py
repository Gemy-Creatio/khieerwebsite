
from django import forms
from main import models


class TopicForm(forms.ModelForm):
    class Meta:
        model = models.TopicGreen
        fields = '__all__'
        exclude = ('is_paid',)
        labels = {
            'name': 'عنوان التحدى',
            'filed': 'مجال التحدى',
            'target': 'من هي الفئة المستهدفة في هذه التحدى',
            'number_target': 'كم عدد الفئة المستهدفة',
            'description': 'صف لنا التحدى بالتفصيل موضحًا فيها النقاط الجوهرية التي تحتاج إلى تدخل',
            'effect': 'في حال تم حل هذه التحدى بتوقعك ماهو الأثر الذي ستحققه أو الاسهامات التي ستقدمها',
        }

