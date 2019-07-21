from django import forms
from Movieapp.models import Movies
class MoviesForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields='__all__'
