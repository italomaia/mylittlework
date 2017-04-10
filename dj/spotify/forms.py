from django import forms
from django.forms import widgets
from django.core.validators import MinLengthValidator
import requests
from .ext_api import SPOTIFY_API
from urllib.parse import urlencode


class SearchForm(forms.Form):
    q = forms.CharField(
        widget=widgets.TextInput(
            attrs={
                'placeholder': 'Search...',
                'class': 'form-control'
            }
        ),
        validators=[MinLengthValidator(1)])
    type = forms.ChoiceField(
        initial='track',
        widget=widgets.HiddenInput(),
        choices=(
            ('track', 'Track'),
            ('album', 'Album'),
            ('artist', 'Artist'),
            ('playlist', 'Playlist'),
        ))

    def query_api(self):
        clean_data = self.cleaned_data
        url = SPOTIFY_API['search'] + urlencode(clean_data)
        return requests.get(url)
