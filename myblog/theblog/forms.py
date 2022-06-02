from django import forms
from .models import  Post, Category , ProfileModel  #model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


choice = Category.objects.all().values_list('name' , 'name')
select_list =[]
for i in choice:
    select_list.append(i)
#cats = [('coding', 'coding'), ('AI', 'AI'), ('python', 'python'),('Macine Learning', 'Macine Learning')]
class PostForm (forms.ModelForm):
    class Meta :
        model =Post
        fields= ('title' , 'title_tag' , 'author' , 'category' ,'snippet', 'body',"header_image")

        widgets = {
            
            'category' : forms.Select(choices = select_list),
            'author' : forms.TextInput(attrs={'value':'', 'id':'author_id', 'type':'hidden'}),
        }
        

class EditForm (forms.ModelForm):
    class Meta :
        model = Post
        fields= ('title' , 'title_tag'  , 'category' ,'snippet', 'body',"header_image")

        widgets = {
            'title' : forms.TextInput(),
            'title_tag' : forms.TextInput(),
            'category' : forms.Select(choices = select_list),
            'body' : forms.Textarea(),
            
        }
        
