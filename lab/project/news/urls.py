from django.contrib import admin
from django.urls import re_path, path
from news import views
from .views import ArticleDetailView, ArticleView, HashtagView, RubrikaDetailView, RubrikaView

app_name = 'news'

urlpatterns = [
    path('', views.index, name="index"),
    
    path('rubric_detail/<int:rubric_id>/', RubrikaDetailView.rubric_detail, name='rubric_detail'),
    path('news_detail/<int:news_id>/', ArticleDetailView.news_detail, name='news_detail'),
    
    path('createRubrika/', RubrikaView.as_view(), name="createRubrika"),
    path('delete-rubrika/<int:rubrika_id>/', RubrikaView.delete_rubrika, name='delete_rubrika'),
    
    path('createHashtag/', HashtagView.as_view(), name="createHashtag"),
    path('delete-hashtag/<int:hashtag_id>/', HashtagView.delete_hashtag, name='delete_hashtag'),
    
    path('createArticle/', ArticleView.as_view(), name="createArticle"),
    path('delete-article/<int:article_id>/', ArticleView.delete_article, name='delete_article'),
    
    path('admin', admin.site.urls),
]
