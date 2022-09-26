from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import BlogUser
from django import forms

class CreateUserForm(UserCreationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Nazwa użytkownika"}))
  email = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Email"}))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Hasło"}))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Potwierdź hasło"}))

  groups_list = Group.objects.all()
  try:
    regular_users = groups_list[0]
    extended_users = groups_list[1]
    admins = groups_list[2]
  except:
    print('groups dont exist')
    regular_users = 'regular_users'
    extended_users = 'extended_users'
    admins = 'regular_users'


  choice_list = [(regular_users, 'Zwykły użytkownik'),(extended_users, 'Użytkownik+ (dodawanie treści)')]
  permissions = forms.ChoiceField(choices= choice_list, widget=forms.RadioSelect)

  class Meta:
    model = User
    fields = ["username", "email", "password1", "password2",]

class EditUserProfileForm(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput())
  email = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Email"}))
  first_name = forms.CharField(required=False, widget=forms.TextInput())
  description = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":2}), max_length=200)

  class Meta:
    model = BlogUser
    fields = '__all__'
    exclude =['user']  
  
class EditProfilePicture(forms.ModelForm):

  class Meta:
    model = BlogUser
    fields = ["profile_picture"]

