from django.forms import ModelForm, CharField, ChoiceField, RadioSelect, TextInput, Select
from .models import Author, Quote


class AuthorForm(ModelForm):

    fullname = CharField(min_length=3, max_length=25, required=True)
    born_date = CharField(max_length=30)
    born_location = CharField(max_length=150)
    description = CharField(max_length=1500)
    
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
        
        
class AddAuthorForm(ModelForm):
    fullname = CharField(min_length=3, max_length=25, widget=TextInput(attrs={"class": "form-control"}))
    born_date = CharField(max_length=30, widget=TextInput(attrs={"class": "form-control"}))
    born_location = CharField(max_length=150, widget=TextInput(attrs={"class": "form-control"}))
    description = CharField(max_length=4000, widget=TextInput(attrs={"class": "form-control"}))
    
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
        
        
class AddQuoteForm(ModelForm):
    CHOICES = Author.objects.all()
    choices_list = list(enumerate(CHOICES, 1))    
    print(choices_list)           
    quote = CharField(min_length=3, max_length=1500, required=True, widget=TextInput(attrs={"class": "form-control"}))  
    author = ChoiceField(choices=choices_list, widget=Select(attrs={"class": "form-control"})) 
    tags = CharField(max_length=100, widget=TextInput(attrs={"class": "form-control"}))
    
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']
          