# # account/forms.py
# from django import forms
# from .models import User
#
# class UserCreationForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('email', 'phone_number', 'name', 'password')
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user
