from django import forms
from persons.models import owner

class ContactForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    active_notifications = forms.BooleanField()

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        print("some")
        pass

    class Meta:
        model = owner
        fields = ('name', 'user__email', 'notifications')
        exclude = ['user']
