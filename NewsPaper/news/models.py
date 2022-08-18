from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser
from news.resources import CATEGORY_CHOICES, news, article
from django.db.models import Sum
from django.urls import reverse
from django.core.cache import cache


class Author(models.Model):
    # pass
    author_user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name = 'Автор')
    rating_author = models.SmallIntegerField(default=0, verbose_name = 'Рейтинг автора')

    def upgrate_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating_post'))
        pRat = 0
        pRat += postRat.get('postRating')

        postComment = self.author_user.comment_set.aggregate(commentRating=Sum('rating_comment'))
        cRat = 0
        cRat += postComment.get('commentRating')

        self.rating_author = pRat * 3 + cRat
        self.save()

    def __str__(self):
        return '{}'.format(self.author_user)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def get_absolute_url(self):
        return reverse('author', args=[str(self.id)])

class Category(models.Model):
    # pass
    name_of_category = models.CharField(max_length=64, unique=True, verbose_name = 'Категория')
    subscribe = models.ManyToManyField(User, through='Subscribers', blank=True)

    def __str__(self):
        return self.name_of_category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Subscribers (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name = 'Пользователь')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name = 'Категория')

    class Meta:
        verbose_name = 'Пользователь/Категория'
        verbose_name_plural = 'Пользователи/Категории'

    def __str__(self):
        return f' {self.user}: {self.category}'

class Post (models.Model):
    #pass
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name = 'Автор')
    vid = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=news, verbose_name = 'Статья или Новость')
    data_create_post = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата создания')
    title_post = models.CharField(max_length=64, verbose_name = 'Заголовок')
    text_post = models.TextField(verbose_name = 'Текст')
    rating_post = models.SmallIntegerField(default=0, verbose_name = 'Рейтинг статьи')
    category = models.ManyToManyField(Category, through='PostCategory', verbose_name = 'Категория')
    isUpdated = models.BooleanField(default=False)

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        return self.text_post[0:123] + '...'

    def __str__(self):
        return f'{self.title_post}: {self.data_create_post.strftime("%m/%d/%Y")}: {self.category}'

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'post-{self.pk}')  # затем удаляем его из кэша, чтобы сбросить его

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-data_create_post']

class PostCategory(models.Model):
    # pass
    post_through = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name = 'Статья')
    category_through = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = 'Категория')

    def __str__(self):
        return f' {self.category_through}: {self.post_through}'

    class Meta:
        verbose_name = 'Категория/статья'
        verbose_name_plural = 'Категории/статьи'

class Comment(models.Model):
    # pass
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name = 'Статья')
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Автор')
    text_comment = models.TextField(verbose_name = 'Комментарий')
    data_create_comment = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата комментария')
    rating_comment = models.SmallIntegerField(default=0, verbose_name = 'Рейтинг комментария')

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()

    def __str__(self):
        return f'{self.data_create_comment.strftime("%m/%d/%Y")}: {self.text_comment}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
