from django import forms
from .models import QuoteRequest


# class QuoteRequestForm(forms.ModelForm):
#     class Meta:
#         model = QuoteRequest
#         fields = ['first_name', 'last_name', 'service', 'phone', 'message']
#
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
#             'service': forms.Select(attrs={'class': 'form-control'}, choices=[
#                 ('Construction', 'Construction'),
#                 ('Renovation', 'Renovation'),
#                 ('Interior Design', 'Interior Design'),
#                 ('Exterior Design', 'Exterior Design'),
#                 ('Painting', 'Painting'),
#             ]),
#             'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
#             'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': 2}),
#         }
#
#     submit = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'btn btn-primary py-3 px-4', 'type': 'submit', 'value': 'Appointment'}))


class QuoteRequestForm(forms.Form):
    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    services = forms.ChoiceField(choices=[
        ('', 'Select Your Services'),
        ('construction', 'Construction'),
        ('renovation', 'Renovation'),
        ('interior_design', 'Interior Design'),
        ('exterior_design', 'Exterior Design'),
        ('painting', 'Painting')
    ], widget=forms.Select(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=15,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'cols': 30, 'rows': 2}))
