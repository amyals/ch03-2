from django import forms

from .models import Post, Comment, Like

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class LikeForm(forms.ModelForm):

    class Meta:
        model = Like
        fields = ('author', )
