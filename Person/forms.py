from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
class FormSignUp(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['cin','first_name','last_name','username','email','password1','password2']
    def save(self,commit=True):
        user=super(FormSignUp,self).save(commit)
        return user
        

    