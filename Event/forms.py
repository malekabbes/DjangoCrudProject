
# from django import forms
from .models import Event
from django import forms
from django.forms import ModelForm, Textarea

class AddForm(ModelForm):
    class Meta:
        model=Event
        fields=("title","description","organizer","state","nbe_participant","category","event_date")
        widgets={'description':Textarea(
            attrs={'cols':20,'rows':10}
        )}

  