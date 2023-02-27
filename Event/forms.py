
# from django import forms
from datetime import date
from .models import Event
from django import forms
from django.forms import ModelForm, Textarea

class AddForm(ModelForm):
    class Meta:
        model=Event
        fields=("title","description","organizer","state","nbe_participant","category","event_date","image")
        # image=forms.ImageField()
        widgets={'description':Textarea(
            attrs={'cols':20,'rows':10}
        )}
        help_text={
            'title':"Your title here",
        }
        error_messages={
            'title':{
            'max_length':"This event's title is too long",
            }
            }
        event_date=forms.DateField(label="Date de l'evenement",initial=date.today,
                                   widget=forms.DateInput(attrs={'type':'date',
                                                          'class':'form-control',
                                                          'placeholder':'Date d\'event'}))
            
        

  