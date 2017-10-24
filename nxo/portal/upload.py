from django import forms
from .models import File



class FileUpload(forms.ModelForm):
    class Meta:
        model = File
        fields = ('name', 'path', )


