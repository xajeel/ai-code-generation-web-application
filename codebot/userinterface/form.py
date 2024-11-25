from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email'})),

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # Customize individual field placeholders
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = ''
        
        
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].label = ''
        
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = ''
        
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label = ''

        # Optionally customize help texts
        self.fields['password1'].help_text = '''
            <ul class="form-help-text">
                <li>Password must contain at least 8 characters.</li>
                <li>Password must contain at least one lowercase letter (a-z).</li>
                <li>Password must contain at least one digit (0-9).</li>
                <li>Password must contain at least one special character (e.g., !@#$%^&*).</li>
            </ul>
'''
        self.fields['password2'].help_text = '<span class="form-help-text">Enter the same password as above.</span>'