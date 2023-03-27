from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api/', views.polls_list, name='list-api'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>-api/', views.polls_detail, name='detail-api'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:pk>/choices/', views.choices_list, name='results-api'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]