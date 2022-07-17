from tkinter import Widget
from django import forms
from myapp.models import Order

class InterestForm(forms.Form):
    INTEREST_OPTION = [(0, 'No'), (1, 'Yes')]
    
    interested = forms.CharField(label='Interest', widget=forms.RadioSelect(choices=INTEREST_OPTION))
    #interested = forms.ChoiceField(label='interested', widget=forms.RadioSelect, choices=INTEREST_OPTION)
    levels = forms.IntegerField(label= "Levels" ,initial=1)
    comments = forms.CharField(required=False, label = 'Additional Comments', widget=forms.Textarea)
    

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [ 'student', 'course', 'levels', 'order_date']
        widgets = {'student': forms.RadioSelect(), 'order_date': forms.SelectDateWidget}