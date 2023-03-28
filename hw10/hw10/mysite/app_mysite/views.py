from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
#from django.views.generic import TemplateView

from .forms import AuthorForm, QuoteForm
from .models import Author, Quote

# Create your views here.

# class HomePageView(TemplateView):
#     template_name = 'quotes.html'

def main(request):
    return render(request, 'app_mysite/index.html', context={'title': 'My Site'})


def quotes(request):
    quotes = Quote.objects.all()
    return render(request, 'app_mysite/quotes.html', context={'title': 'My Site', 'quotes': quotes})


def authors(request):
    if request.GET.get("id", ''):
        authors = Author.objects.all().filter(id=request.GET.get("id", ''))
    else:
        authors = Author.objects.all()
    return render(request, 'app_mysite/authors.html', context={'title': 'My Site', 'authors': authors})

def tags(request):
    search_tag = request.GET.get("tag", '')
    if search_tag:
        quotes = Quote.objects.filter(tags__icontains=search_tag)
    else:
        quotes = Quote.objects.all()
        
    return render(request, 'app_mysite/tags.html', context={'title': 'My Site', 'quotes': quotes})


@login_required
def add_author(request):        
    form_author = AuthorForm(instance=Author())
    if request.method == "POST":
        form_author = AuthorForm(request.POST, instance=Author()) 
        if form_author.is_valid():
            form_author.save() 
            return redirect(to='app_mysite:authors')  
    
    return render(request, 'app_mysite/add_author.html', context={'title': 'My Site', 'form_author': form_author})

@login_required
def add_quote(request):
    form_quote = QuoteForm(instance=Quote())
    if request.method == "POST":
        my_request = request.POST.dict()
        my_request["tags"] = my_request["tags"].replace(r", ", " ").replace(r",", " ").strip().split(" ")
        form_quote = QuoteForm(my_request, instance=Quote()) 
        if form_quote.is_valid():
            form_quote.save() 
            return redirect(to='app_mysite:quotes') 
    
    return render(request, 'app_mysite/add_quote.html', context={'title': 'My Site', 'form_quote': form_quote})    

        