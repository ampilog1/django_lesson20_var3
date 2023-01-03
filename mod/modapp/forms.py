from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Название')
    email = forms.EmailField(label='email работодателя')
    message = forms.CharField(label='Описание вакансии')