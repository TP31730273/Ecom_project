# -*- coding: utf-8 -*-

from django import forms

from app.models import UserAccount


# -----------------------------------------------------------------------------
# User
# -----------------------------------------------------------------------------

class UserCreationForm(forms.ModelForm):
    """Custom User"""

    class Meta():
        model = UserAccount
        fields = [
            "email",
            "password",
            "username",
            "image",
           
            
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        username = cleaned_data.get("username")

        if not email :
            raise forms.ValidationError(
                "Please add email."
            )
        if not username :
            raise forms.ValidationError(
                "Please add email."
            )
        if not password :
            raise forms.ValidationError(
                "Please add Password."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class UserChangeForm(forms.ModelForm):
    """Custom form to change User"""

    class Meta():
        model = UserAccount

        fields = [
            "email",
            "password",
            "username",
            "image",
           
        ]

    def clean(self):
        cleaned_data = super(UserChangeForm,self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        username = cleaned_data.get("username")
        

        if not email :
            raise forms.ValidationError(
                "Please add email."
            )
        if not password :
            raise forms.ValidationError(
                "Please add Password."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance