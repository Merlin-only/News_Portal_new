from django import forms
from .models import Post, Author

class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['author', 'vid', 'title_post', 'text_post', 'category']

class AuthorForm(forms.ModelForm):
   class Meta:
       model = Author
       fields = ['author_user']