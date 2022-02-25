from django.urls import path
from . import views

urlpatterns = [
    path('category_form', views.category_form),
    path('get_category', views.get_category),
    path('delete_category/<int:category_id>', views.delete_category),
    path('update_category/<int:category_id>', views.category_update_form),


    path('news_form', views.news_form),
    path('get_news', views.get_news),
    path('delete_news/<int:news_id>', views.delete_news),
    path('update_news/<int:news_id>', views.news_update_form),


    path('get_category_user', views.show_categories),
    path('get_news_user', views.show_news),


]