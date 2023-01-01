from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUserView, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('creator-post/<str:pk>/', views.creatorPostPage, name='creator-post'),
    path('video/<str:pk>/', views.videoViewingPage, name='video-view'),
    path('create/video/', views.videoUploadingFormPage, name='upload-video')
]
