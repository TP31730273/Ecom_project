# -*- coding: utf-8 -*-

from django import forms

from app.models import Category


# -----------------------------------------------------------------------------
# User
# -----------------------------------------------------------------------------

class CategoryCreationForm(forms.ModelForm):
    """Custom Category"""

    class Meta():
        model = Category
        fields = [
            "category_name",
            
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CategoryCreationForm, self).clean()
        category_name = cleaned_data.get("category_name")
       
        if not category_name :
            raise forms.ValidationError(
                "Please add category_name."
            )
    

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class CategoryChangeForm(forms.ModelForm):
    """Custom form to change category"""

    class Meta():
        model = Category

        fields = [
            "category_name",
        
        ]

    def clean(self):
        cleaned_data = super(CategoryChangeForm,self).clean()
        category_name = cleaned_data.get("category_name")
        
        

        if not category_name :
            raise forms.ValidationError(
                "Please add category_name."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance