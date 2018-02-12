from django import forms
from . import models


class MyForm(forms.Form):
    text = forms.CharField(max_length=100)


# class UploadFileForm(forms.ModelForm):
#     class Meta:
#         model = models.UploadFileModel
#         fields = "__all__"


class UploadFileForm(forms.Form):
    file = forms.FileField()