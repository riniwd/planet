from django.forms import ModelForm, TextInput, NumberInput
from .models import Data


class WriteForm(ModelForm):
    class Meta:
        model = Data
        fields = ['tel', 'count']

        widgets = {
            "tel": NumberInput(attrs={
                'placeholder': '7-000-000-00-00',
                'oninput':'maxL(this, 11)'
            }),

            "count": NumberInput(attrs={
                'placeholder': '3-35'
            }),
        }

