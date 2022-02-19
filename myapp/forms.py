from dataclasses import fields
from django import forms
from myapp.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["name", "email", "id_no", "img_profile"]
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'id_no': forms.NumberInput(attrs={'class': 'form-control'}),
                   'img_profile': forms.FileInput(attrs={'class': 'form-control'}),
                   }
