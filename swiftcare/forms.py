import password
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


User = get_user_model()

#login form
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


#registration form
class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        help_text="",  # Remove help text
        widget=forms.TextInput(attrs={"placeholder": "Enter your username"})  #  Optional
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

    def save(self, commit=True):
      user = super().save(commit=False)
      user.set_password(self.cleaned_data['password'])
      if commit:
            user.save()
            return user


      if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

