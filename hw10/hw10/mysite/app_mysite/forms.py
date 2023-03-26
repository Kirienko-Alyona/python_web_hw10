from django.forms import DateField, DateInput, ModelForm, CharField, TextInput, Select, ModelChoiceField, JSONField, Textarea
from .models import Author, Quote
from django.contrib.postgres.fields import ArrayField
        
        
class AddAuthorForm(ModelForm):
    
    fullname = CharField(min_length=3, max_length=25, widget=TextInput(attrs={"class": "form-control"}))
    born_date = DateField(widget=DateInput(attrs={"type":"date", "class":"form-control"}))
    #born_date = CharField(max_length=30, widget=TextInput(attrs={"class": "form-control"}))
    born_location = CharField(max_length=150, widget=TextInput(attrs={"class": "form-control"}))
    description = CharField(max_length=4000, widget=Textarea(attrs={"class": "form-control"}))
    
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
        
        
class AddQuoteForm(ModelForm):
    quote = CharField(max_length=1500, required=True, widget=TextInput(attrs={"class": "form-control"}))  
    author = ModelChoiceField(queryset=Author.objects.all(), required=True, widget=Select(attrs={"class": "form-control"}))
    tags = JSONField(max_length=100, required=False, widget=TextInput(attrs={"class": "form-control"}))
    
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']
          