from django.forms import ModelForm
from .models import s_data

class addForm(ModelForm):
    class Meta:
        model = s_data
        fields = '__all__'