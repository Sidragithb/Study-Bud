from django.forms import ModelForm
from .models import Room,User
from django.contrib.auth.forms import UserCreationForm



class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']
 
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description'] 
        exclude=['host','participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username', 'email','bio'] 
