from django import forms


class OrderForm(forms.Form):
    total_price = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'TotalPrice','name':'totalprice0','id':'totalprice'}))
    delivery_address = forms.CharField(max_length=500,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address','name':'address0'}))
    comments = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Comments','name':'comment','id':'comment'}))
