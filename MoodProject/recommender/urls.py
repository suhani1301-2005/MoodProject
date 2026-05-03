from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('history/', views.history, name='history'),
    path('analytics/', views.analytics, name='analytics'),  # ✅ Analytics route
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('playlist/<str:name>/', views.playlist_view, name='playlist'),
    path('mood-input/', views.mood_input_view, name='mood_input'),  # ✅ AI mood input form
    path('mood-detect/', views.mood_detect_view, name='mood_detect'),  # ✅ AI mood detection
]