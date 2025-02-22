from django.urls import path
from . import views

urlpatterns = [
    # Function-based view
    path('message/', views.simple_message_view, name='simple_message'),

    # Class-based view
    path('', views.HomePageView.as_view(), name='home'),

    # URL with parameter
    path('greet/<str:name>/', views.greet_view, name='greet'),
    
    path('dynamic/', views.dynamic_content_view, name='dynamic_content'),
]