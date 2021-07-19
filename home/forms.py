from django import forms
from  .models import Ems

class EmsForm(forms.ModelForm):
    class Meta:
        model=Ems
        fields="__all__"
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'contact':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-m-2'}),
            'date':forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date','class':'form-control'}),
            'email':forms.EmailField.widget(attrs={'class':'form-control'})
        }