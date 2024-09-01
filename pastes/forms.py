from django import forms
from django.forms import ValidationError
from django.utils.baseconv import BASE64_ALPHABET

from .models import Paste


class AddPasteForm(forms.ModelForm):
    class Meta:
        model = Paste
        fields = ["text", "url", "expired_at"]

        widgets = {
            "expired_at": forms.TextInput(attrs={"type": "datetime-local"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set `custom_url` and `expiration_date` to not required
        self.fields["url"].required = False
        self.fields["expired_at"].required = False

    def clean_url(self):
        url = self.cleaned_data["url"]
        if not (set(url) <= set(BASE64_ALPHABET)):
            raise ValidationError(
                "Only English characters, numbers, hyphens and underscores are allowed."
            )

        return url
