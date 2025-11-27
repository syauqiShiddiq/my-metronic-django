from django.urls import path
from . import views

# app_name ini PENTING agar bisa dipanggil di template menggunakan {% url 'polls:index' %}
app_name = 'polls'

urlpatterns = [
    # Halaman Index (Daftar Pertanyaan)
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),

    # Halaman Detail (Form Voting)
    # Generic view mengharapkan primary key dipanggil sebagai 'pk'
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # Halaman Results (Hasil Voting)
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # Proses Vote (Function based view)
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]