from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Article, Category, Tag, Comment
from .forms import CreateCommentForm
from django.core.paginator import Paginator


def home_view(request):
    articles = Article.objects.all().order_by('-id')
    pagination = Paginator(articles[:3], 2)
    page = request.GET.get('page')
    article = pagination.get_page(page)
    lst = []

    for page in range(1, article.paginator.num_pages+1):
        lst.append(page)

    context = {
        'list': lst,
        'page': page,
        'article': article,
        'articles': articles,
    }
    return render(request, 'index.html', context)


def article_list(request):
    articles = Article.objects.order_by('-id')
    search = request.GET.get('search')
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    if search:
        articles = articles.filter(title__icontains=search)
    if cat:
        articles = articles.filter(category__category__exact=cat)
    if tag:
        articles = articles.filter(tag__tag__exact=tag)

    context = {
        'articles': articles
    }
    return render(request, 'blog.html', context)


def article_detail(request, slug):
    articles = Article.objects.order_by('-id')
    article = get_object_or_404(Article, slug=slug)
    last_3_posts = Article.objects.order_by('-id')[:3]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    comments = Comment.objects.filter(article__slug__exact=slug).order_by('-id')
    form = CreateCommentForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.article = article
        comment.author = request.user
        comment.save()
        return redirect(f'/detail/{article.slug}#comments')

    context = {
        'tags': tags,
        'form': form,
        'article': article,
        'articles': articles,
        'comments': comments,
        'categories': categories,
        'last_3_posts': last_3_posts,
    }
    return render(request, 'blog-single.html', context)
