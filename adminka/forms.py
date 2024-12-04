from django import forms
from front.models import *

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['type', 'title', 'description', 'file', 'user', 'img']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'img', 'role']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name', 'img']  # Укажите поля, которые нужно редактировать

