from django import forms
from path.models import Post

class SimpleForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
        	'class': 'col-sm-4',
            'class': 'form-control',
            'placeholder': 'Enter city...'
        }
    ))

    class Meta:
        model = Post
        fields = ('post',)
