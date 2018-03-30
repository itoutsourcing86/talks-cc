from django.urls import path
from . import views


urlpatterns = [
    path('', views.TalkListView.as_view(), name='list'),
    path('lists/<slug:slug>/', views.TalkDetailView.as_view(), name='detail'),
    path('create/', views.TalkCreateView.as_view(), name='create'),
    path('update/<slug:slug>/', views.TalksUpdateView.as_view(), name='update'),
]
