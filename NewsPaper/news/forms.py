from django import forms
from .models import Post, Author, Category

class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['author', 'vid', 'title_post', 'text_post', 'category']

class AuthorForm(forms.ModelForm):
   class Meta:
       model = Author
       fields = ['author_user']

class CategoryForm(forms.ModelForm):
   class Meta:
       model = Category
       fields = ['name_of_category']