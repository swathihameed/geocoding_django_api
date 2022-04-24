# import the standard Django Forms
# from built-in library
from django import forms
   
# creating a form 
class InputForm(forms.Form):
   
    address = forms.CharField(max_length = 200)
   
    output_format = forms.ChoiceField(choices=[('JSON','json'),('XML','xml')], widget=forms.RadioSelect)