from django import forms
from .models import Comment, Subscribe

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ('name', 'email')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email...'}),
        }

    def __init__(self, *args, **kwargs):
        super(SubscribeForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['email'].label = ""