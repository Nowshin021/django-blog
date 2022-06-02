"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

from .views import HomeView,ArticleDetailView,AddPostView, UpdatePostView, DeletePostView,AddCategoryView,CategoryView
#name of the view class --> HomeView

urlpatterns = [
    #path('', views.home , name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>',ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/',AddPostView.as_view(), name ='add-post'),

    


    path('add_category/',AddCategoryView.as_view(), name ='add-category'),
    path('article/edit/<int:pk>' , UpdatePostView.as_view(), name ='update-post'),
    path('article/<int:pk>/delete' , DeletePostView.as_view(), name ='delete-post'),
    path('category/<str:cats>/', CategoryView , name ='category')
    
]   
