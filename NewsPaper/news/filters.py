from django_filters import FilterSet, ModelChoiceFilter, CharFilter, AllValuesFilter
from django_filters import DateTimeFilter, ModelMultipleChoiceFilter
from .models import Category, Author, Post

class NewsFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name = 'postcategory__category_through',
        queryset = Category.objects.all(),
        label = 'Категория',
        empty_label = 'все категории',
    )

    news_date = DateTimeFilter(
        field_name = 'post__data_create_post',
        lookup_expr = 'gte',
        label = 'Новости, опубликованные после даты:',
    )
    author = ModelMultipleChoiceFilter(
        field_name = 'author__author_user',
        queryset = Author.objects.all(),
        label = 'Автор',
        conjoined = True,
    )

    news_title = CharFilter(
        field_name='title_post',
        lookup_expr='iexact',
        label = 'Заголовок',
        #empty_label = 'Вбирете заголовок',
    )
#AllValuesFilter
    # class Meta:
    #     model = Post
    #     fields = {
    #         'title_post': ['icontains'],
    #         'rating_post': [
    #             'lt',  # цена должна быть меньше или равна указанной
    #             'gt',  # цена должна быть больше или равна указанной
    #         ],
    #     }