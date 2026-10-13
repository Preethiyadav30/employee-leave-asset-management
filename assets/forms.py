from django import forms
from .models import Asset


class AssetRequestForm(forms.ModelForm):

    class Meta:
        model = Asset
        fields = ["asset_type"]