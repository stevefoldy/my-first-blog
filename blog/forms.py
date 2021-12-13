from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
            'title': TextInput(attrs={'class': "form-control", 'placeholder': 'Post title'}),
            'text': Textarea(attrs={'class': "form-control", 'placeholder': 'Post description'}),
        }