from django import forms
from .models import Bill, BillItem
from products.models import Product

class BillItemForm(forms.ModelForm):
    class Meta:
        model = BillItem
        fields = ['product', 'quantity', 'price']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-select product-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control quantity-input', 'min': 1}),
            'price': forms.NumberInput(attrs={'class': 'form-control price-input', 'step': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.filter(status='active').order_by('name')
        self.fields['product'].empty_label = 'Select a product'
        self.fields['price'].required = True

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity') or 0
        if quantity <= 0:
            raise forms.ValidationError('Quantity must be at least 1.')
        return quantity

    def clean_price(self):
        price = self.cleaned_data.get('price') or 0
        if price <= 0:
            raise forms.ValidationError('Price must be greater than 0.')
        return price

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        price = cleaned_data.get('price')
        if product and not price:
            cleaned_data['price'] = product.price
        return cleaned_data

BillItemFormSet = forms.inlineformset_factory(
    Bill,
    BillItem,
    form=BillItemForm,
    extra=3,
    can_delete=True,
    min_num=1,
    validate_min=True,
)

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['customer', 'notes']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
