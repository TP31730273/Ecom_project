# # -*- coding: utf-8 -*-

# from django import forms

# from ..models import SocialCode


# # -----------------------------------------------------------------------------
# # SocialCode
# # -----------------------------------------------------------------------------

# class SocialCodeCreationForm(forms.ModelForm):
#     """Custom SocialCodeCreationForm"""

#     class Meta():
#         model = SocialCode
#         fields = [
#             "code",
#             "meaning"
#         ]

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def clean(self):
#         cleaned_data = super(SocialCodeCreationForm, self).clean()
#         code = cleaned_data.get("code")
#         meaning = cleaned_data.get("meaning")

#         if not code :
#             raise forms.ValidationError(
#                 "Please add code."
#             )
#         if not meaning :
#             raise forms.ValidationError(
#                 "Please add meaning."
#             )
#     def save(self, commit=True):
#         instance = super().save(commit=False)

#         if commit:
#             instance.save()

#         return instance


# class SocialCodeChangeForm(forms.ModelForm):
#     """Custom form to change SocialCode"""

#     class Meta():
#         model = SocialCode

#         fields = [
#             "code",
#             "meaning"
#         ]

#     def clean(self):
#         cleaned_data = super(SocialCodeChangeForm, self).clean()
#         code = cleaned_data.get("code")
#         meaning = cleaned_data.get("meaning")

#         if not code :
#             raise forms.ValidationError(
#                 "Please add code."
#             )
#         if not meaning :
#             raise forms.ValidationError(
#                 "Please add meaning."
#             )

#     def save(self, commit=True):
#         instance = super().save(commit=False)

#         if commit:
#             instance.save()

#         return instance