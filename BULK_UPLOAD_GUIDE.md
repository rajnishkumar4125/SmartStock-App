# Bulk Upload System - Quick Start Guide

## 📋 Overview
SmartStock App now includes a bulk upload feature that allows you to import large quantities of products and customers using CSV files. This guide will help you get started.

---

## 🚀 Getting Started

### Step 1: Access Bulk Upload
- **Products**: Go to Products page → Click "Bulk Upload" button
- **Customers**: Go to Customers page → Click "Bulk Upload" button

### Step 2: Download Sample CSV (Optional)
- Click "Download Sample CSV" to get a template file
- This shows you the exact format required

### Step 3: Prepare Your CSV File
- Use Excel or any text editor to create your CSV file
- Ensure all required columns are present
- See format requirements below

### Step 4: Upload File
- Click "Choose File" and select your CSV
- Click "Upload CSV" button
- Wait for processing to complete

### Step 5: Review Results
- See summary statistics
- Check successful imports
- Review any failed rows with error messages

---

## 📊 Product CSV Format

### Required Columns:
```
name,sku,category,price,stock_quantity,reorder_level
```

### Optional Columns:
```
description,status
```

### Complete Example:
```csv
name,sku,category,price,stock_quantity,reorder_level,description,status
Laptop Pro 15,LAPTOP-001,Electronics,1299.99,25,5,High-performance laptop for professionals,active
Wireless Mouse,MOUSE-002,Electronics,49.99,100,20,Ergonomic wireless mouse,active
USB-C Cable,CABLE-003,Accessories,19.99,500,100,5m USB-C charging cable,active
```

### Validation Rules:
- **name**: Max 200 characters, required
- **sku**: Max 50 characters, must be unique, required
- **category**: Will be created if doesn't exist, required
- **price**: Must be a positive number with up to 2 decimals
- **stock_quantity**: Must be a non-negative integer
- **reorder_level**: Must be a non-negative integer
- **description**: Optional, any text
- **status**: Optional, must be one of: `active`, `inactive`, `discontinued`

---

## 👥 Customer CSV Format

### Required Columns:
```
name,email,phone,address,city,country
```

### Optional Columns:
```
state,postal_code
```

### Complete Example:
```csv
name,email,phone,address,city,country,state,postal_code
John Smith,john.smith@example.com,9876543210,123 Main Street,New York,USA,NY,10001
Sarah Johnson,sarah.j@example.com,5551234567,456 Oak Avenue,Los Angeles,USA,CA,90001
Michael Chen,m.chen@example.com,6179876543,789 Pine Road,Boston,USA,MA,02101
```

### Validation Rules:
- **name**: Max 200 characters, required
- **email**: Must be valid email format, must be unique, required
- **phone**: Must be 10-15 digits (numbers only), required
- **address**: Required
- **city**: Max 100 characters, required
- **country**: Max 100 characters, required
- **state**: Optional, max 100 characters
- **postal_code**: Optional, max 20 characters

---

## ⚠️ Common Issues & Solutions

### Issue: "File must be a CSV file"
**Solution**: Ensure you're uploading a `.csv` file, not Excel (.xlsx) or other formats.

### Issue: "File size must be less than 5MB"
**Solution**: Split your data into multiple CSV files (max 5MB each).

### Issue: "Missing required fields: name, sku, category..."
**Solution**: Check CSV headers match exactly (case-sensitive):
- ✅ Correct: `name,sku,category`
- ❌ Incorrect: `Name,SKU,Category`

### Issue: "SKU 'PROD-001' already exists"
**Solution**: Use unique SKU values. Check existing products first.

### Issue: "Invalid email: user@invalid"
**Solution**: Ensure email format is correct (e.g., user@example.com)

### Issue: "Invalid phone: 123 (must be 10-15 digits)"
**Solution**: Phone must contain only digits and be 10-15 characters long.

### Issue: "Email 'user@example.com' already exists"
**Solution**: Use unique email addresses. Check existing customers first.

---

## 📈 Understanding Results

### Summary Statistics:
- **Total Processed**: Total rows in CSV (excluding header)
- **Successful**: Number of records created successfully
- **Failed**: Number of records that failed validation
- **Success Rate**: Percentage of successful imports

### Success Table:
Shows all successfully imported records with:
- Row number in CSV
- Product name or Customer name
- SKU or Email (depending on import type)

### Failed Table:
Shows all failed imports with:
- Row number in CSV
- Reason for failure (detailed error message)

---

## 💡 Tips & Best Practices

### Before Uploading:
1. ✅ Validate your data in Excel before uploading
2. ✅ Check for duplicate values (SKU for products, email for customers)
3. ✅ Ensure all required columns are present
4. ✅ Test with a small sample first (5-10 rows)

### Data Preparation:
1. ✅ Use consistent data format
2. ✅ Remove extra spaces and special characters
3. ✅ Validate email addresses
4. ✅ Use proper phone number format (digits only)

### After Upload:
1. ✅ Review the results page carefully
2. ✅ Check failed rows for error messages
3. ✅ Fix issues and re-upload failed records
4. ✅ Verify data in the product/customer list

---

## 🔄 Workflow Example

### Scenario: Import 100 Products

1. **Prepare CSV** (Excel/Google Sheets)
   - Add product data
   - Validate all required columns present
   - Save as CSV

2. **Upload**
   - Navigate to Products → Bulk Upload
   - Select your CSV file
   - Click Upload

3. **Review Results**
   - 95 successful ✅
   - 5 failed ❌
   - Success Rate: 95%

4. **Fix Failures**
   - Note failed row numbers and reasons
   - Correct data in your CSV
   - Reupload

5. **Verify**
   - Go to Products list
   - Confirm all 100 products are present
   - Check stock levels if needed

---

## 📞 Support

If you encounter issues:

1. Check the error message for specific details
2. Review the validation rules above
3. Compare your CSV with the sample format
4. Contact administrator for database issues

---

## 🔒 Security & Limitations

### Security:
- Only authenticated users can upload files
- Files are validated before processing
- Maximum file size: 5MB
- CSV files are not stored permanently

### Limitations:
- One file at a time
- Maximum 5MB per file
- CSV format only (not Excel)
- Processing is synchronous (may take time for large files)

### Future Enhancements:
- Async processing for faster uploads
- Excel file support
- Preview before uploading
- Batch operations after upload

---

## 📝 CSV Template Examples

### Minimal Product CSV (Required fields only):
```csv
name,sku,category,price,stock_quantity,reorder_level
Product A,SKU-001,Category A,10.00,100,20
Product B,SKU-002,Category B,20.00,50,10
```

### Full Product CSV (All fields):
```csv
name,sku,category,price,stock_quantity,reorder_level,description,status
Product A,SKU-001,Category A,10.00,100,20,Description here,active
Product B,SKU-002,Category B,20.00,50,10,Another description,inactive
```

### Minimal Customer CSV (Required fields only):
```csv
name,email,phone,address,city,country
John Doe,john@example.com,9876543210,123 St,City,USA
Jane Smith,jane@example.com,9876543211,456 Ave,City,USA
```

### Full Customer CSV (All fields):
```csv
name,email,phone,address,city,country,state,postal_code
John Doe,john@example.com,9876543210,123 St,City,USA,State,12345
Jane Smith,jane@example.com,9876543211,456 Ave,City,USA,State,54321
```

---

## 🎓 Video Tutorial

For a visual guide, refer to the flowchart in `CSV_UPLOAD_FLOWCHART.md` which shows:
- Step-by-step process flow
- Validation checkpoints
- Error handling paths
- Results reporting

---

**Last Updated**: 2024  
**Version**: 1.0  
**Status**: Active
