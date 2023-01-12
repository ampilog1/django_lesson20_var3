from django import forms

from modapp.models import Vacancy


class ContactForm(forms.Form):
    name = forms.CharField(label='Название')
    email = forms.EmailField(label='email')
    message = forms.CharField(label='Сообщение')


class PostForm(forms.ModelForm):
    name = forms.CharField(label='Название')
    class Meta:
        model = Vacancy
        fields = '__all__'


