from django.forms import ModelForm
from .models import Reviews, Product
class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['posted_by']

