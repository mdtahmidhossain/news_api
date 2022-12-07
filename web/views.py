from django.shortcuts import render
from django.http import JsonResponse
from django.views import generic
from datetime import datetime, timedelta
from web.models import Source, Article
from decouple import config
import requests


class NewsListView(generic.ListView):
    paginate_by = 20
    model = Article
    context_object_name = 'news_list'
    template_name = 'news_list.html'

    def get_queryset(self):
        get_data_from_api()
        return Article.objects.all().prefetch_related('source_set').order_by(
            '-published_at'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def to_article(list):
    for dist in list:
        article_object = Article(
            author=dist['author'],
            title=dist['title'],
            description=dist['description'],
            url=dist['url'],
            url_to_image=dist['urlToImage'],
            published_at=dist['publishedAt'],
            content=dist['content'],
        )
        article_object.save()
        api_id = dist['source']['id']
        name = dist['source']['name']
        source, created = Source.objects.get_or_create(
            api_id=api_id,
            name=name,
            defaults={'api_id': api_id, 'name': name},
        )
        source.article.add(article_object)
        source.save()


def json_endpoint(request):
    return JsonResponse(
        list(Article.objects.all().prefetch_related('source_set').order_by(
            '-published_at'
        ).values()[0:100]),
        safe=False
    )


def home(request):
    return render(request, 'home.html')


def get_data_from_api():
    date_from = datetime.today() + timedelta(days=-1)
    print(Article.objects.count())
    if (Article.objects.count() > 0):
        date_from = Article.objects.all().order_by(
            '-published_at'
        ).first().published_at + timedelta(minutes=1)
    date_to = date_from + timedelta(days=1)
    params = {
        'apiKey': config('NEWS_API_KEY'),
        'q': 'tesla',
        'from': date_from.isoformat(),
        'to': date_to.isoformat(),
        'sortBy': 'publishedAt'
    }
    api_response = requests.get(config('NEWS_API_URL'), params=params)
    to_article(api_response.json()['articles'])
