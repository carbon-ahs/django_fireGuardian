from django import forms
from .models import officeDetail
'''
from .models import ModelName
class ModelNameForm(forms.ModelForm):
    class Meta:
        model = ModelName
        fields = '__all__'
'''
class officeDetailForm(forms.ModelForm):
    class Meta:
        model = officeDetail
        fields = '__all__'
        '''
        widgets = {
            'office_size': forms.NumberInput(attrs={'label': 'Your office Size? :','required': True}),
            'office_type': forms.FileInput(attrs={'label': 'Your office type? :', 'required': True}),
        }
        '''