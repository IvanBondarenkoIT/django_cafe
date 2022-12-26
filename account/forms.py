from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.check_password(password):
                raise forms.ValueError('Login or password is incorrect!')
        return super().clean()


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', )

    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] == data['password2']:
            return data['password2']
        raise forms.ValidationError('Passwords is not match')

