from django.shortcuts import render
from django.views.generic import ListView , DetailView,CreateView,UpdateView, DeleteView
from .models import Post,Category
from .forms import PostForm,EditForm,ProfileModel
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
#def home(request):
#   return render(request, 'home.html', {})


#homeview with class view using class view and detail view
class HomeView(ListView):
    model=Post
    template_name = "home.html"
    #ordering = ['-id']
    ordering = ['-post_date']


class ArticleDetailView(DetailView):
    model =Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model=Post
    form_class = PostForm
    template_name = 'add_post.html'



class UpdatePostView(UpdateView):
    model =Post
    form_class = EditForm
    template_name = 'update_post.html'
    


class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url = reverse_lazy('home')



class AddCategoryView(CreateView):
    model=Category
    fields= '__all__'
    template_name = 'add_category.html'










#basic functional view view (not class based views )
#cats == from urls.py cats
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    
    return render(request, 'category.html', {'cats' : cats, 'category_posts' :category_posts, 'Category' : Category.objects.all() })
    



