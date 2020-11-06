from django import forms
from .models import Comment, Subscribe
from mptt.forms import TreeNodeChoiceField

class NewCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].required = False
        self.fields['parent'].label = ''
        self.fields['parent'].widget.attrs.update({'class': 'd-none'})


    class Meta:
        model = Comment
        fields = ('name','parent', 'email', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'cols':20, 'rows':5})
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