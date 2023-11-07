from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from apphabits.forms import StyleFormMixin
from users.models import User


class UserForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm_profile(StyleFormMixin,  UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()