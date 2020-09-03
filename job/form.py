from django import forms
from .models import Apply, Job

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email', 'portfolio', 'cv', 'cover_litter']
        
class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('slug','published_at','owner',)