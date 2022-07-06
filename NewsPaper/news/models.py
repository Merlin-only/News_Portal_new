from django.db import models
from django.contrib.auth.models import User
from news.resources import CATEGORY_CHOICES, news, article
from django.db.models import Sum


class Author(models.Model):
    # pass
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.SmallIntegerField(default=0)

    def upgrate_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating_post'))
        pRat = 0
        pRat += postRat.get('postRating')

        postComment = self.author_user.comment_set.aggregate(commentRating=Sum('rating_comment'))
        cRat = 0
        cRat += postComment.get('commentRating')

        self.rating_author = pRat * 3 + cRat
        self.save()


class Category(models.Model):
    # pass
    name_of_category = models.CharField(max_length=64, unique=True)


class Post (models.Model):
    #pass
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    vid = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=news)
    data_create_post = models.DateTimeField(auto_now_add=True)
    title_post = models.CharField(max_length=64)
    text_post = models.TextField()
    rating_post = models.SmallIntegerField(default=0)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        self.text_post[0:123] + '...'


class PostCategory(models.Model):
    # pass
    post_through = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_through = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    # pass
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    data_create_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.SmallIntegerField(default=0)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()
