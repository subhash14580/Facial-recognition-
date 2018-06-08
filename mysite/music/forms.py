from django import forms
from models import Students, Log


class StudentForm(forms.ModelForm):
    id = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'enter the Student id'
    }))
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'enter the Name'
    }))

    class Meta:
        model = Students
        fields = ('id', 'name', 'image', )


class LogForm(forms.ModelForm):
    class Meta1:
        model = Log
        fields = ('refid','date','in_time','out_time')
