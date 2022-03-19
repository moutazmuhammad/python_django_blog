from django import forms
from .models import Post, Comment, Category, Tags

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':2})) # to change the size of text area field
    tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Tags.objects.all())	
    class Meta:
        model = Post
        fields = ('title', 'body', 'image', 'category', 'tags')


class EditPostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':2})) # to change the size of text area field
    tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Tags.objects.all())	
    class Meta:
        model = Post
        fields = ('title', 'body', 'image', 'category', 'tags')

class CommentForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Write Comment ...'})) # to change the size of text area field
    class Meta:
        model = Comment
        fields = ('body',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ('name',)
