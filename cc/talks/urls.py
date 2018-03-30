from django.urls import path
from . import views


urlpatterns = [
    path('', views.TalkListView.as_view(), name='list'),
    path('lists/<slug:slug>/', views.TalkDetailView.as_view(), name='detail')
]