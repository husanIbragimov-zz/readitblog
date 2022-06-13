from django.shortcuts import render
from readit_app.models import Article

from django.shortcuts import render
from .models import Team


def team_view(request):
    articles = Article.objects.order_by('-id')
    member = Team.objects.all()
    context = {
        'members': member,
        'articles': articles
    }
    return render(request, 'about.html', context)
