from django import forms
from django.forms import ModelForm
from . models import Userprofiles



class UpdateprofileForm(ModelForm):
    class Meta:
        model = Userprofiles
        exclude = ['user']

        