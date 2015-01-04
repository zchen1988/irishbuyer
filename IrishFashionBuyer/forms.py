from django import forms


class OrderForm(forms.Form):
    total_price = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Total Price','name':'totalprice0','id':'totalprice'}))
    total_original_price = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Total Original Price','name':'totaloriprice0','id':'totaloriprice'}))
    total_weight = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Total Weight','name':'totalweight0','id':'totalweight'}))
    delivery_address = forms.CharField(max_length=500,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address','name':'address0'}))
    comments = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Comments','name':'comment','id':'comment'}))

class OrderFormAgent(forms.Form):
    total_price = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Total Price','name':'totalprice0','id':'totalprice'}))
    delivery_address = forms.CharField(max_length=500,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address','name':'address0'}))
    comments = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Comments','name':'comment','id':'comment'}))
