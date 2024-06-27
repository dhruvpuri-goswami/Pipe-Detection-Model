from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()
    multiplier = forms.IntegerField(help_text="A numeric value to multiply with the pipe count.")
