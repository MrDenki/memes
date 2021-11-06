from django import forms
from base.models import Users, CollectionsMemes


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('email', 'nickname', 'password')
        widgets = {
            'email': forms.EmailInput(),
            'nickname': forms.TextInput(),
            'password': forms.PasswordInput(),
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = CollectionsMemes
        fields = ('description', 'photo', 'user')
