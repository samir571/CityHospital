from django.shortcuts import render, redirect
from .forms import CategoryForm, NewsForm
from django.contrib import messages
from .models import Category, News
from accounts.auth import admin_only, user_only
from django.contrib.auth.decorators import login_required
import os


# def profile(request):
#     return render(request, 'news/profile.html')
#

@login_required
@admin_only
def category_form(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category added successfully')
            return redirect("/news/get_category")
        else:
            messages.add_message(request, messages.ERROR,'Unable to add category')
            return render(request, 'news/category_form.html',{'form_category':form})
    context={
        'form_category' : CategoryForm,
        'activate_category':'active'
    }

    return render(request, 'news/category_form.html', context)


@login_required
@admin_only
def get_category(request):
    categories = Category.objects.all().order_by('-id')
    context={
        'categories': categories,
        'activate_category' :'active'

    }
    return render(request, 'news/get_category.html',context)


@login_required
@admin_only
def delete_category(request, category_id):
    category=Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS,'Category deleted Successfully')
    return redirect('/news/get_category')


@login_required
@admin_only
def category_update_form(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category updated successfully')
            return redirect("/news/get_category")
        else:
            messages.add_message(request, messages.ERROR,'Unable to update category')
            return render(request, 'news/category_update_form.html',{'form_category':form})
    context={
        'form_category' : CategoryForm(instance=category),
        'activate_category':'active'
    }

    return render(request, 'news/category_update_form.html', context)


# _______________________NEWS PART______________________________
@login_required
@admin_only
def news_form(request):
    if request.method == "POST":
        form = NewsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'News added successfully')
            return redirect("/news/get_news")
        else:
            messages.add_message(request, messages.ERROR,'Unable to add news')
            return render(request, 'news/news_form.html',{'form_news':form})
    context={
        'form_news' : NewsForm,
        'activate_news':'active'
    }

    return render(request, 'news/news_form.html', context)

@login_required
@admin_only
def get_news(request):
    news = News.objects.all().order_by('-id')
    context={
        'news': news,
        'activate_news' :'active'

    }
    return render(request, 'news/get_news.html',context)

@login_required
@admin_only
def delete_news(request, news_id):
    news=News.objects.get(id=news_id)
    os.remove(news.news_image.path)
    news.delete()
    messages.add_message(request, messages.SUCCESS,'News deleted Successfully')
    return redirect('/news/get_news')

@login_required
@admin_only
def news_update_form(request, news_id):
    news = News.objects.get(id=news_id)
    if request.method == "POST":
        if request.FILES.get('news_image'):
            os.remove(news.news_image.path)
        form = NewsForm(request.POST,request.FILES, instance=news)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'News updated successfully')
            return redirect("/news/get_news")
        else:
            messages.add_message(request, messages.ERROR,'Unable to update news')
            return render(request, 'news/news_update_form.html',{'form_news':form})
    context={
        'form_news' : NewsForm(instance=news),
        'activate_news':'active'
    }
    return render(request, 'news/news_update_form.html', context)


@login_required
def show_categories(request):
    categories = Category.objects.all().order_by('-id')
    context={
        'categories':categories,
        'activate_category_user': 'active'

    }
    return render(request, 'news/show_categories.html', context)

@login_required
def show_news(request):
    news = News.objects.all().order_by('-id')
    context={
        'news':news,
        'activate_news_user':'active'

    }
    return render(request, 'news/show_news.html', context)





