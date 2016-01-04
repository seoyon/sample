from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist

from files.models import *

class UploadForm(forms.Form):
    file = forms.FileField(label = 'File to upload')
    
    def clean_file(self):
        if self.cleaned_data.has_key('file'):
            file = self.cleaned_data['file']
            try:
                File.objects.get(name = file.name.replace(" ", "_").replace(",", "_"))
                raise ValidationError("This file already exists.")
            except ObjectDoesNotExist:
                return file
        raise ValidationError("This field is required")
