from django import forms

class MyForm(forms.Form):
    text = forms.CharField(max_length=100)


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
