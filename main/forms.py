
from django import forms
from main import models


class TopicForm(forms.ModelForm):
    class Meta:
        model = models.TopicGreen
        fields = '__all__'
        labels = {
            'name': 'عنوان القضية',
            'filed': 'مجال القضية',
            'target': 'من هي الفئة المستهدفة في هذه القضية',
            'number_target': 'كم عدد الفئة المستهدفة',
            'description': 'صف لنا القضية بالتفصيل موضحًا فيها النقاط الجوهرية التي تحتاج إلى تدخل',
            'effect': 'في حال تم حل هذه القضية بتوقعك ماهو الأثر الذي ستحققه أو الاسهامات التي ستقدمها',
        }

