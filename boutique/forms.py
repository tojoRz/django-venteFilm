from django.forms import ModelForm, TextInput, EmailInput
from .models import Contact
from django.forms.utils import ErrorList


class ParagraphErrorList(ErrorList):

    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return
        return '<div class="errorList text-danger">%s</div>' % ''.join(['<p class="smallerror">%s</p>' % e for e in self])  

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["nom", "email"]
        widget = {
            'nom': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'})
        }


