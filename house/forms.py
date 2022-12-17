from django import forms
from .models import House


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['title', 'image', 'address', 'price',
                  'rooms', 'kitchen', 'balcony', 'description', 'washroom']

    def clean(self):
        data = self.cleaned_data
        print(data)
