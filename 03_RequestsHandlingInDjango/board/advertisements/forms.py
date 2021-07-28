from django import forms


class AdvertisementForm(forms.Form):
    title = forms.CharField()
    discription = forms.CharField()