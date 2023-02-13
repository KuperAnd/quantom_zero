from django.shortcuts import render
from apps.blog.models import BlogCategory, Article

#классический контроллер,соединяет то что видит пользователь с нашей логикой(кодом,скрытая логика у нас в моделях models.py)
# достать все данные из базы данных
def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    return render(request, 'blog/category/list.html', {'categories': blog_categories})


def article_list(request, category_id):
    articles = Article.objects.filter(category=category_id)
    return render(request, 'blog/article/list.html', {'articles': articles})


def article_view(request, category_id, article_id):
    article = Article.objects.get(id=article_id)
    category = BlogCategory.objects.get(id=category_id)
    return render(request, 'blog/article/view.html', {'article':article, 'category': category})