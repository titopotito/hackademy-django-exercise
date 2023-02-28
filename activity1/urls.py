from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('profile', views.profile_view, name='profile'),
    path('profile/edit', views.edit_profile_view, name='edit_profile'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_user, name='logout')
]
