from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Full Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'})
    )
    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'})
    )
    phone = forms.CharField(
        max_length=20,
        label='Phone Number',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'})
    )
    subject = forms.CharField(
        max_length=150,
        label='Subject',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the subject'})
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your message here', 'rows': 5})
    )
