from django import forms
from .models import Information

class Adddetail (forms.ModelForm):
    class Meta():
        model = Information
        fields = '__all__'
        widgets = {
            'name ' : forms.TextInput(attrs={'class':'input','autofocus':True}),
            'email' : forms.EmailInput(attrs={'class':'inpt','autofocus':True}),
            'phoneno' : forms.NumberInput(attrs={ 'maxlength': 15, 'required': True, 'type': 'number',}),

        }


