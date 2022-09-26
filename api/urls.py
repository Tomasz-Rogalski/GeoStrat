from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    #Home
    path('', views.api, name='api'),
    path('get_topic/(<int:topic_id>)/', views.get_topic, name='topic'),
    path('get_topics/', views.get_topics, name='get_topics'),
    # path('add_topic/', views.add_topic, name='add_topic'),        
]