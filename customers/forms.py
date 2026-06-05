from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address', 'city', 'state', 'postal_code', 'country']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }

class BulkCustomerUploadForm(forms.Form):
    """Form for bulk customer CSV upload."""
    csv_file = forms.FileField(
        label='CSV File',
        help_text='Upload a CSV file with customer data. Required columns: name, email, phone, address, city, country',
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
