from django import forms
from basicapp.models import Messages

class FormMessage(forms.ModelForm):
    mymessage = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Messages
        fields = '__all__'