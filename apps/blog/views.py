from django.shortcuts import render
from apps.blog.models import BlogCategory, Article, Tag


#классический контроллер,соединяет то что видит пользователь с нашей логикой(кодом,скрытая логика у нас в моделях models.py)
# достать все данные из базы данных
def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    return render(request, 'blog/category/list.html', {'categories': blog_categories})


def article_list(request, category_id):
    articles = Article.objects.filter(category=category_id)
    category = BlogCategory.objects.get(id=category_id)
    return render(request, 'blog/article/list.html', {'articles': articles, 'category': category})


def article_view(request, category_id, article_id):
    article = Article.objects.get(id=article_id)
    category = BlogCategory.objects.get(id=category_id)
    return render(request, 'blog/article/view.html', {'article': article, 'category': category})


def tag_search_article_list(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    #article = Article.objects.filter(tags=tag_id)
    articles = Article.objects.filter(tags__in=[tag_id])
    return render(request, 'blog/article/tag_search.html', {'articles': articles, 'tag': tag})

