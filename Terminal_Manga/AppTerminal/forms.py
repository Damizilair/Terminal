from django import forms

class MangasFormulario(forms.Form):
    mangas = forms.CharField()
    tomos = forms.IntegerField()