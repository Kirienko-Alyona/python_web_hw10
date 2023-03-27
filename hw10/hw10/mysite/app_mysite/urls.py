from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'app_mysite'

urlpatterns = [
    #path('', views.main, name='main'),
    path('', views.quotes, name='quotes'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('quotes/', views.quotes, name='quotes'),
    path('authors/', views.authors, name='authors'),
    path('add_author/', views.add_author, name='add_author'),
    #path("quotes/", LogoutView.as_view(template_name="quotes.html"), name='logout'),
]