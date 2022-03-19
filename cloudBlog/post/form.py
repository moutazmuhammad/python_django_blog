from django import forms
from .models import Post, Comment, Category

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':2})) # to change the size of text area field
    class Meta:
        model = Post
        fields = ('title', 'body', 'image', 'category')


class EditPostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':2})) # to change the size of text area field
    class Meta:
        model = Post
        fields = ('title', 'body', 'image', 'category')

class CommentForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Write Comment ...'})) # to change the size of text area field
    class Meta:
        model = Comment
        fields = ('body',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
