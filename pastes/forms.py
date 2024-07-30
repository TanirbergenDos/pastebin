from django import forms

from .models import Paste


class AddPasteForm(forms.ModelForm):
    class Meta:
        model = Paste
        fields = ["text", "url", "expired_at"]

        widgets = {
            "url": forms.TextInput(attrs={"required": False}),
            "expired_at": forms.TextInput(attrs={"type": "datetime-local"}),
        }

    def __init__(self, *args, **kwargs):
        super(AddPasteForm, self).__init__(*args, **kwargs)
        # Set `custom_url` to not required
        self.fields["url"].required = False
