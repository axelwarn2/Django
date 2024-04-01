from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from .forms import ArticleForm, HashtagForm, RubrikaForm
from .models import Article, Hashtag, Rubrika

def index(request):
    rubrics = Rubrika.objects.all()
    news_list = Article.objects.order_by('-id').all()
    return render(request, 'news/index.html', {'rubrics': rubrics, 'news_list': news_list})

class RubrikaDetailView:
    def rubric_detail(request, rubric_id):
        rubrics = Rubrika.objects.all()
        articles = Article.objects.filter(rubNum_id=rubric_id)
        return render(request, 'news/rubric_detail.html', {'rubrics': rubrics, 'articles': articles})

class ArticleDetailView(View):
    def news_detail(request, news_id):
        news = get_object_or_404(Article, pk=news_id)
        hashtags = news.hashtags.all()
        return render(request, 'news/news_detail.html', {'news': news, 'hashtags': hashtags})

class RubrikaView(View):
    def get(self, request):
        rubrics = Rubrika.objects.all()
        form = RubrikaForm()
        return render(request, 'news/createRubrika.html', {'rubrics': rubrics, 'form': form})

    def post(self, request):
        if request.method == "POST":
            form = RubrikaForm(request.POST)
            if form.is_valid():
                if not Rubrika.objects.filter(title=form.cleaned_data['title']).exists():
                    form.save()
                    return redirect('news:createRubrika')
                else:
                    return redirect('news:createRubrika')

        form = RubrikaForm()
        data = {'form': form}
        return render(request, "news/createRubrika.html", data)

    def delete_rubrika(request, rubrika_id):
        rubrika = Rubrika.objects.get(pk=rubrika_id)
        rubrika.delete()
        return redirect('news:createRubrika')
    
class HashtagView(View):
    def get(self, request):
        hashtags = Hashtag.objects.all()
        form = HashtagForm()
        return render(request, 'news/createHashtag.html', {'hashtags': hashtags, 'form': form})

    def post(self, request):
        if request.method == "POST":
            form = HashtagForm(request.POST)
            if form.is_valid():
                if not (Hashtag.objects.filter(title=form.cleaned_data['title']).exists()):
                    form.save()
                    return redirect('news:createHashtag')
                else:
                    return redirect('news:createHashtag')
        form = HashtagForm()
        data = {'form': form}
        return render(request, "news/createHashtag.html", data)

    def delete_hashtag(request, hashtag_id):
        hashtag = Hashtag.objects.get(pk=hashtag_id)
        hashtag.delete()
        return redirect('news:createHashtag')

class ArticleView(View):
    def get(self, request):
        articles = Article.objects.all()
        form = ArticleForm()
        return render(request, 'news/createArticle.html', {'articles': articles, 'form': form})

    def post(self, request):
        if request.method == "POST":
            form = ArticleForm(request.POST)
            if form.is_valid():
                if not(Article.objects.filter(title=form.cleaned_data['title']).exists()):
                    form.save()
                    return redirect('news:createArticle')
                else:
                    return redirect('news:createArticle')
        form = ArticleForm()
        data = {'form': form}
        return render(request, "news/createArticle.html", data)

    def delete_article(request, article_id):
        article = Article.objects.get(pk=article_id)
        article.delete()
        return redirect('news:createArticle')