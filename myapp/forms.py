from django import forms
from myapp.models import Order

class InterestForm(forms.Form):
    INTEREST_OPTION = [(0, 'No'), (1, 'Yes')]
    
    interested = forms.CharField(label='Interest', widget=forms.RadioSelect(choices=INTEREST_OPTION))
    levels = forms.IntegerField(label= "Levels" ,min_value=1)
    comments = forms.CharField( label = 'Additional Comments', widget=forms.Textarea)