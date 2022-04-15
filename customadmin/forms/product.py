# -*- coding: utf-8 -*-

from django import forms

from app.models import Product


# -----------------------------------------------------------------------------
# User
# -----------------------------------------------------------------------------

class ProductCreationForm(forms.ModelForm):
    """Custom Product"""

    class Meta():
        model = Product
        fields = [
            "product_name",
            "product_description",
            "product_price",
            "product_image",
            "product_category",
            "seller",
            "is_active",
            
            
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ProductCreationForm, self).clean()
        product_name = cleaned_data.get("product_name")
        product_description = cleaned_data.get("product_description")
        product_price = cleaned_data.get("product_price")
        product_image = cleaned_data.get("product_image")
        product_category = cleaned_data.get("product_category")
        seller = cleaned_data.get("seller")
        is_active = cleaned_data.get("is_active")
        
       
        if not product_name :
            raise forms.ValidationError(
                "Please add product_name."
            )
        if not product_description :
            raise forms.ValidationError(
                "Please add product_description."
            )
        if not product_price :
            raise forms.ValidationError(
                "Please add product_price."
            )
        if not product_image :
            raise forms.ValidationError(
                "Please add product_image."
            )
        if not product_category :
            raise forms.ValidationError(
                "Please add product_category."
            )
        if not seller :
            raise forms.ValidationError(
                "Please add seller."
            )
        if not is_active :
            raise forms.ValidationError(
                "Please add is_active."
            )
        
    

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class ProductChangeForm(forms.ModelForm):
    """Custom form to change category"""

    class Meta():
        model = Product

        fields = [
            "product_name",
            "product_description",
            "product_price",
            "product_image",
            "product_category",
            "seller",
            "is_active",
        
        ]

    def clean(self):
        cleaned_data = super(ProductChangeForm, self).clean()
        product_name = cleaned_data.get("product_name")
        product_description = cleaned_data.get("product_description")
        product_price = cleaned_data.get("product_price")
        product_image = cleaned_data.get("product_image")
        product_category = cleaned_data.get("product_category")
        seller = cleaned_data.get("seller")
        is_active = cleaned_data.get("is_active")
        
       
        if not product_name :
            raise forms.ValidationError(
                "Please add product_name."
            )
        if not product_description :
            raise forms.ValidationError(
                "Please add product_description."
            )
        if not product_price :
            raise forms.ValidationError(
                "Please add product_price."
            )
        if not product_image :
            raise forms.ValidationError(
                "Please add product_image."
            )
        if not product_category :
            raise forms.ValidationError(
                "Please add product_category."
            )
        if not seller :
            raise forms.ValidationError(
                "Please add seller."
            )
        if not is_active :
            raise forms.ValidationError(
                "Please add is_active."
            )
        
    def save(self, commit=True):
        
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance