from xml.dom import ValidationErr
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.core.exceptions import ValidationError




class Person(AbstractUser):

    def cin_length(v):
        if len(str(v))!=8:
            raise ValidationError("Your CIN must have 8 characters !")
        return v
        # ou bien

        
    cin = models.IntegerField('CIN',primary_key=True,validators=[
        cin_length
    ])
    class Meta:
       verbose_name=("Evenement")

    

    email = models.EmailField()
    def validemail(self):
        if not self.email.endswith('@esprit.tn'):
            raise ValidationErr('Email {email} must end with @esprit.tn ',params={"email":self.email})
