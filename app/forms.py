from django import forms

class PowerPointUploadForm(forms.Form):
    powerpoint_file = forms.FileField(label='Upload PowerPoint File')
