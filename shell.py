Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
(venv) alevtinaefremova@MacBook-Pro-Alevtina NewsPaper % python manage.py makemigrations
Migrations for 'news':
  news/migrations/0001_initial.py
    - Create model Author
    - Create model Category
    - Create model Post
    - Create model PostCategory
    - Add field category to post
    - Create model Comment
(venv) alevtinaefremova@MacBook-Pro-Alevtina NewsPaper % python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, news, sessions
Running migrations:
  Applying news.0001_initial... OK
(venv) alevtinaefremova@MacBook-Pro-Alevtina NewsPaper % python manage.py shell
Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> User1 = User.objects.create_user(username = "Суходрищева Фёкла Сирановна")
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'User' is not defined
>>> User1 = User.objects.create_user(username = 'Суходрищева Фёкла Сирановна")
  File "<console>", line 1
    User1 = User.objects.create_user(username = 'Суходрищева Фёкла Сирановна")
                                                ^
SyntaxError: unterminated string literal (detected at line 1)
>>> User1 = User.objects.create_user(username='Суходрищева Фёкла Сирановна')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'User' is not defined
>>> ^D
now exiting InteractiveConsole...
(venv) alevtinaefremova@MacBook-Pro-Alevtina NewsPaper % from news.models import *
from: can't read /var/mail/news.models
(venv) alevtinaefremova@MacBook-Pro-Alevtina NewsPaper % python manage.py shell
Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from news.models import *
>>> User1 = User.objects.create_user(username='Суходрищева Фёкла Сирановна')
>>> User2 = User.objects.create_user(username='Пупкин Аристарх Понтилеевич')
>>> Author.objects.create(author_user=User1)
<Author: Author object (1)>
>>> Author.objects.create(author_user=User2)
<Author: Author object (2)>
>>> Category.objects.create(name_of_category='Спорт')
<Category: Category object (1)>
>>> Category.objects.create(name_of_category='Политика')
<Category: Category object (2)>
>>> Category.objects.create(name_of_category='Образование')
<Category: Category object (3)>
>>> Category.objects.create(name_of_category='Наука')
<Category: Category object (4)>
>>> Category.objects.create(name_of_category='Развлечения')
<Category: Category object (5)>
>>> author = Author.objects.get(id=1)
>>> author
<Author: Author object (1)>
>>> Post.object.create(author=author, vid='AR', title='sometitle, text='somebigtext')
  File "<console>", line 1
    Post.object.create(author=author, vid='AR', title='sometitle, text='somebigtext')
                                                                                   ^
SyntaxError: unterminated string literal (detected at line 1)
>>> Post.objects.create(author=author, vid='AR', title='Сенсация!!!', text='На улице Лизюкова обнаружено НЛО')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/alevtinaefremova/PycharmProjects/News_Portal/venv/lib/python3.10/site-packages/django/db/models/manager.py", line 85, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/Users/alevtinaefremova/PycharmProjects/News_Portal/venv/lib/python3.10/site-packages/django/db/models/query.py", line 512, in create
    obj = self.model(**kwargs)
  File "/Users/alevtinaefremova/PycharmProjects/News_Portal/venv/lib/python3.10/site-packages/django/db/models/base.py", line 559, in __init__
    raise TypeError(
TypeError: Post() got an unexpected keyword argument 'title'
>>> Post.objects.create(author=author, vid='AR', title='sometitle', text='sometext')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/alevtinaefremova/PycharmProjects/News_Portal/venv/lib/python3.10/site-packages/django/db/models/manager.py", line 85, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/Users/alevtinaefremova/PycharmProjects/News_Portal/venv/lib/python3.10/site-packages/django/db/models/query.py", line 512, in create
    obj = self.model(**kwargs)
  File "/Users/alevtinaefremova/PycharmProjects/News_Portal/venv/lib/python3.10/site-packages/django/db/models/base.py", line 559, in __init__
    raise TypeError(
TypeError: Post() got an unexpected keyword argument 'title'
>>> 
>>> Post.objects.create(author=author, vid='AR', title_post='Сенсация!!!', text_post='На улице Лизюкова обнаружено НЛО')
<Post: Post object (1)>
>>> author = Author.objects.get(id=2)
>>> 
>>> author
<Author: Author object (2)>
>>> Post.objects.create(author=author, vid='AR', title_post='В городе найдены динозавры', text_post='На улице Лихтенштейна при раскорках были обнаружены останки динозавров')
<Post: Post object (2)>
>>> Post.objects.create(author=author, vid='NW', title_post='Телепортация возможна!', text_post='5 июля 2022 года американские ученые изобрели телепорт и переместились из штата Аризона  в Антаркутиду')
<Post: Post object (3)>
>>> Post.objects.get(id=1).title_post
'Сенсация!!!'
>>> Post.objects.get(id=1).category.add(Category.objects.get(id=1)
... ^D
now exiting InteractiveConsole...
(venv) alevtinaefremova@MacBook-Pro-Alevtina NewsPaper % python manage.py shell
Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> Post.objects.get(id=1).title_post
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'Post' is not defined
>>> from news.models import *
>>> Post.objects.get(id=1).title_post
'Сенсация!!!'
>>> Post.objects.get(id=1).category.add(Category.objects.get(id=1))
>>> Post.objects.get(id=1).category.add(Category.objects.get(id=3))
>>> Post.objects.get(id=1).category.add(Category.objects.get(id=5))
>>> Post.objects.get(id=2).category.add(Category.objects.get(id=2))
>>> Post.objects.get(id=2).category.add(Category.objects.get(id=4))
>>> Post.objects.get(id=3).category.add(Category.objects.get(id=3))
>>> Post.objects.get(id=3).category.add(Category.objects.get(id=5))
>>> Comment.objects.create(post_comment=Post.objects.get(id=1), user_comment=Author.objects.get(author_user=User1), text_comment='Всё это фигня')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'User1' is not defined
>>> Comment.objects.create(post_comment=Post.objects.get(id=1), user_comment=Author.objects.get(id=1).author_user, text_comment='Всё это фигня')
<Comment: Comment object (1)>
>>> Comment.objects.create(post_comment=Post.objects.get(id=2), user_comment=Author.objects.get(id=2).author_user, text_comment='Не может этого быть!')
<Comment: Comment object (2)>
>>> Comment.objects.create(post_comment=Post.objects.get(id=3), user_comment=Author.objects.get(id=1).author_user, text_comment='Да ладно')
<Comment: Comment object (3)>
>>> Comment.objects.create(post_comment=Post.objects.get(id=1), user_comment=Author.objects.get(id=2).author_user, text_comment='А доказательства есть?')
<Comment: Comment object (4)>
>>> Comment.objects.get(id=1).like()
>>> Comment.objects.get(id=1).like()
>>> Comment.objects.get(id=1).like()
>>> Comment.objects.get(id=1).like()
>>> Comment.objects.get(id=1).like()
>>> Comment.objects.get(id=1).like()
>>> Comment.objects.get(id=1).rating()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Comment' object has no attribute 'rating'
>>> Comment.objects.get(id=1).rating_comment()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: 'int' object is not callable
>>> Comment.objects.get(id=1).rating_comment
6
>>> Comment.objects.get(id=2).like()
>>>  Comment.objects.get(id=2).like()
  File "<console>", line 1
    Comment.objects.get(id=2).like()
IndentationError: unexpected indent
>>>  Comment.objects.get(id=2).like()
  File "<console>", line 1
    Comment.objects.get(id=2).like()
IndentationError: unexpected indent
>>> Comment.objects.get(id=2).like()
>>> Comment.objects.get(id=2).like()
>>> Comment.objects.get(id=2).like()
>>> Comment.objects.get(id=2).like()
>>> Comment.objects.get(id=2).like()
>>> Comment.objects.get(id=2).like()
>>> Comment.objects.get(id=2).dislike()
>>> Comment.objects.get(id=2).dislike()
>>> Comment.objects.get(id=3).like()
>>> Comment.objects.get(id=4).like()
>>> Post.objects.get(id=1).like()
>>> Post.objects.get(id=1).like()
>>> Post.objects.get(id=1).like()
>>> Post.objects.get(id=1).like()
>>> Post.objects.get(id=1).like()
>>> Post.objects.get(id=1).like()
>>> Post.objects.get(id=2).dislike()
>>> Post.objects.get(id=2).dislike()
>>> Post.objects.get(id=2).dislike()
>>> Post.objects.get(id=2).dislike()
>>> Post.objects.get(id=3).dislike()
>>> Post.objects.get(id=4).dislike()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/alevtinaefremova/PycharmProjects/News_Portal/venv/lib/python3.10/site-packages/django/db/models/manager.py", line 85, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/Users/alevtinaefremova/PycharmProjects/News_Portal/venv/lib/python3.10/site-packages/django/db/models/query.py", line 496, in get
    raise self.model.DoesNotExist(
news.models.Post.DoesNotExist: Post matching query does not exist.
>>> Author.objects.get(id=1).upgrate_rating()
>>> rating_author
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'rating_author' is not defined
>>> Author.objects.get(id=1).rating_author
25
>>> Author.objects.get(id=2).upgrate_rating()
>>> Author.objects.get(id=2).rating_author
-9
>>> a = Author.objects.order_by('-rating_author')
>>> a
<QuerySet [<Author: Author object (1)>, <Author: Author object (2)>]>
>>> a = Author.objects.order_by('-rating_author')[:1]
>>> a
<QuerySet [<Author: Author object (1)>]>
>>> for i in a
  File "<console>", line 1
    for i in a
              ^
SyntaxError: expected ':'
>>> for i in a:
...     i.rating_author
...     i.author_user.username
... 
25
'Суходрищева Фёкла Сирановна'
>>> b = Post.objects.order_by('-rating_post')[:1]
>>> b
<QuerySet [<Post: Post object (1)>]>
>>> for i in b:
...     i.data_create_post
...     i.author
...     i.rating_post
...     i.title_post
...     i.preview()
... 
datetime.datetime(2022, 7, 6, 11, 49, 27, 15521, tzinfo=datetime.timezone.utc)
<Author: Author object (1)>
6
'Сенсация!!!'
>>> for i in b:
...     i.data_create_post
...     i.author.username()
... 
datetime.datetime(2022, 7, 6, 11, 49, 27, 15521, tzinfo=datetime.timezone.utc)
Traceback (most recent call last):
  File "<console>", line 3, in <module>
AttributeError: 'Author' object has no attribute 'username'
>>> for i in b:
...     i.author.username
... 
Traceback (most recent call last):
  File "<console>", line 2, in <module>
AttributeError: 'Author' object has no attribute 'username'
>>> for i in b:
...     i.author.author_user.username
... 
'Суходрищева Фёкла Сирановна'
>>> for i in b:
...     i.data_create_post
...     i.author.author_user.username
...     i.rating_post
...     i.title_post
...     i.text_post.preview()
... 
datetime.datetime(2022, 7, 6, 11, 49, 27, 15521, tzinfo=datetime.timezone.utc)
'Суходрищева Фёкла Сирановна'
6
'Сенсация!!!'
Traceback (most recent call last):
  File "<console>", line 6, in <module>
AttributeError: 'str' object has no attribute 'preview'
SyntaxError: invalid decimal literal
