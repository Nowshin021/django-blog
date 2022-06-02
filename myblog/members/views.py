from django.shortcuts import render,get_object_or_404
from .forms import SignupForm,EditProfileForm
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import ListView , DetailView,CreateView,UpdateView, DeleteView
from theblog.models import ProfileModel
from .forms import *



class UserRegisterView(generic.CreateView):
    form_class=SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class=EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class Password_ChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/change-password.html'
    success_url =reverse_lazy('home')


class CreatePublicProfileView(CreateView):
    model=ProfileModel
    form_class=AddProfileInformationForm
    template_name = 'registration/create_public_profile.html'


    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    success_url =reverse_lazy('home')

class PublicProfile(DetailView):
    model=ProfileModel
    template_name = 'registration/public_profile.html'

    def get_context_data(self, *args , **kwargs):
        
        users = ProfileModel.objects.all()
        

        context=super(PublicProfile,self).get_context_data(*args , **kwargs)
        page_user=get_object_or_404(ProfileModel, id=self.kwargs['pk'])
        context['page_user']=page_user
        return context

    


class UpdatePublicProfileView(generic.UpdateView):
    model = ProfileModel
    #form_class=EditInformationForm
    template_name="registration/public_profile_edit.html"
    fields=['bio', 'profile_pic','facebook' ,'twitter', 'twitter','instagram' ,'linkedin']
    success_url = reverse_lazy('home')
 