from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'category', 'description', 'price', 'stock_quantity', 'reorder_level', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
            'stock_quantity': forms.NumberInput(attrs={'step': '1'}),
            'reorder_level': forms.NumberInput(attrs={'step': '1'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class BulkProductUploadForm(forms.Form):
    """Form for bulk product CSV upload."""
    csv_file = forms.FileField(
        label='CSV File',
        help_text='Upload a CSV file with product data. Required columns: name, sku, category, price, stock_quantity, reorder_level',
        widget=forms.FileInput(attrs={
            'accept': '.csv',
            'class': 'form-control',
        })
    )
    
    def clean_csv_file(self):
        csv_file = self.cleaned_data['csv_file']
        
        # Validate file extension
        if not csv_file.name.lower().endswith('.csv'):
            raise forms.ValidationError('File must be a CSV file.')
        
        # Validate file size (max 5MB)
        if csv_file.size > 5 * 1024 * 1024:
            raise forms.ValidationError('File size must be less than 5MB.')
        
        return csv_file
