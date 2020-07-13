from django import forms


class document_file(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    dfiles = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    

    