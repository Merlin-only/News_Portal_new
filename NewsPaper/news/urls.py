from django.urls import path
# Импортируем созданное нами представление
from .views import *


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
    path('', NewsList.as_view(), name='home'),
    path('post/<int:pk>', NewsDetail.as_view(), name='post'),
    path('search/', SearchList.as_view(), name='search'),
    path('create/', PostCreate.as_view(), name='create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('authory/', AuthorList.as_view(), name='authory'),
    path('author_edit/<int:pk>', AuthorProtectedView.as_view(), name='author_edit'),
]
