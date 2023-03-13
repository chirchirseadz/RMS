from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    # path to my profile page
    
    path('profile/',views.profile, name='user_profile'),

    path('profile/update/', views.ProfileUpdate, name='profile_update'),
    # paths to all the user authentication system 
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password/change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_reset'),
    path('password/change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),name='password_change_done'),
    path('password/reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='reset_password'),
    path('password/reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    
]                                                                         