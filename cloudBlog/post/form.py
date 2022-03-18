from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':2})) # to change the size of text area field
    class Meta:
        model = Post
        fields = ('title', 'body', 'image')


class EditPostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':2})) # to change the size of text area field
    class Meta:
        model = Post
        fields = ('title', 'body', 'image')