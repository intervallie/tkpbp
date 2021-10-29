from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm


class MyAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='email',
        widget=forms.TextInput(
            attrs={'autofocus': True, 'placeholder': 'email'})
    )
    password = forms.CharField(
        label='password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'placeholder': 'password'}),
    )


class MyUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['email'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['password1'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['password2'].widget.attrs = {
            'class': 'form-control'
        }
        


    class Meta:
        model = get_user_model()
        fields = ("name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(MyUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
