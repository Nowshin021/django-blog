
from django.urls import path
from . import views
from .views import UserRegisterView,CreatePublicProfileView,UserEditView,Password_ChangeView,PublicProfile,UpdatePublicProfileView
from django.contrib.auth import views as auth_views
#name of the view class --> HomeView



urlpatterns = [
    path('register/', UserRegisterView.as_view(), name ='register'),
    path('edit_profile/', UserEditView.as_view(), name ='edit-profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name = 'registration/change-password.html')),
    path('password/', Password_ChangeView.as_view(),name ='change-password'),
    path('<int:pk>/public_profile/', PublicProfile.as_view(), name="PublicProfile"),
    path('<int:pk>/public_profile_edit/', UpdatePublicProfileView.as_view(), name="UpdatePublicProfileView"),
    path('create_profile', CreatePublicProfileView.as_view(), name='CreatePublicProfileView')
]   
