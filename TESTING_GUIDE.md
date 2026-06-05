# Testing Guide - Bulk Upload Feature

## 🧪 Manual Testing Instructions

### Prerequisites
1. Django development server running: `python manage.py runserver`
2. Logged in as admin or authenticated user
3. Browser at `http://localhost:8000`

---

## ✅ Test Case 1: Product Bulk Upload - Success Scenario

### Test Data (products_test_success.csv)
```csv
name,sku,category,price,stock_quantity,reorder_level,description,status
Dell Laptop,DELL-LAPTOP-001,Electronics,1200.00,30,5,15-inch business laptop,active
HP Mouse,HP-MOUSE-001,Peripherals,45.50,150,30,Wireless optical mouse,active
Lenovo Keyboard,LENOVO-KB-001,Peripherals,79.99,100,20,Mechanical keyboard with RGB,inactive
Samsung Monitor,SAMSUNG-MON-001,Electronics,350.00,25,5,27-inch 4K monitor,active
```

### Steps
1. Navigate to `/products/bulk-upload/`
2. Click "Download Sample CSV" to see template
3. Create file with above data or download and edit sample
4. Click "Choose File" and select CSV
5. Click "Upload CSV"

### Expected Results
- ✅ All 4 products created successfully
- ✅ Summary shows: 4 Successful, 0 Failed, 100% Success Rate
- ✅ Detailed table shows all products with ✓ status
- ✅ Go to Products list and verify all 4 are there

---

## ✅ Test Case 2: Customer Bulk Upload - Success Scenario

### Test Data (customers_test_success.csv)
```csv
name,email,phone,address,city,country,state,postal_code
Alice Johnson,alice.johnson@test.com,5551234567,789 Oak Street,Seattle,USA,WA,98101
Bob Williams,bob.williams@test.com,5559876543,321 Maple Avenue,Portland,USA,OR,97201
Carol Brown,carol.brown@test.com,4155551234,654 Pine Road,San Francisco,USA,CA,94102
David Lee,david.lee@test.com,2125556789,987 Elm Lane,New York,USA,NY,10001
```

### Steps
1. Navigate to `/customers/bulk-upload/`
2. Click "Download Sample CSV"
3. Create or edit file with above data
4. Select and upload CSV
5. Click "Upload CSV"

### Expected Results
- ✅ All 4 customers created successfully
- ✅ Summary shows: 4 Successful, 0 Failed, 100% Success Rate
- ✅ Go to Customers list and verify all 4 are there

---

## ⚠️ Test Case 3: Product Upload - Missing Headers

### Test Data
```csv
name,sku,category,price
Product A,SKU-001,Electronics,99.99
```

### Steps
1. Navigate to `/products/bulk-upload/`
2. Try to upload CSV with missing headers
3. Observe error handling

### Expected Results
- ⚠️ Error message: "Missing required fields: stock_quantity, reorder_level"
- ⚠️ Form stays on upload page
- ⚠️ User can retry with correct format

---

## ⚠️ Test Case 4: Product Upload - Duplicate SKU

### Test Data
```csv
name,sku,category,price,stock_quantity,reorder_level
Product A,TEST-SKU-001,Electronics,99.99,100,20
Product B,TEST-SKU-001,Electronics,149.99,50,10
```

### Steps
1. Navigate to `/products/bulk-upload/`
2. Upload CSV with duplicate SKU in same file
3. Check results page

### Expected Results
- ⚠️ Summary: 1 Successful, 1 Failed
- ⚠️ Success table shows Product A
- ⚠️ Failure table shows: "Row 3: SKU 'TEST-SKU-001' already exists"
- ⚠️ Success rate: 50%

---

## ⚠️ Test Case 5: Customer Upload - Duplicate Email

### Test Data
```csv
name,email,phone,address,city,country
Test User 1,test@example.com,5551234567,Address 1,City 1,USA
Test User 2,test@example.com,5559876543,Address 2,City 2,USA
```

### Steps
1. Navigate to `/customers/bulk-upload/`
2. Upload CSV with duplicate email
3. Check results

### Expected Results
- ⚠️ Summary: 1 Successful, 1 Failed
- ⚠️ Failure reason: "Email 'test@example.com' already exists"

---

## ❌ Test Case 6: Validation Errors - Invalid Price

### Test Data
```csv
name,sku,category,price,stock_quantity,reorder_level
Product A,TEST-PRICE-001,Electronics,-99.99,100,20
```

### Steps
1. Upload CSV with negative price
2. Check results

### Expected Results
- ❌ Row failed with: "Price cannot be negative"

---

## ❌ Test Case 7: Validation Errors - Invalid Stock

### Test Data
```csv
name,sku,category,price,stock_quantity,reorder_level
Product A,TEST-STOCK-001,Electronics,99.99,-100,20
```

### Steps
1. Upload CSV with negative stock quantity
2. Check results

### Expected Results
- ❌ Row failed with: "Stock quantity cannot be negative"

---

## ❌ Test Case 8: Customer Upload - Invalid Email

### Test Data
```csv
name,email,phone,address,city,country
Invalid Email User,not-an-email,5551234567,Address,City,USA
```

### Steps
1. Upload CSV with invalid email
2. Check results

### Expected Results
- ❌ Row failed with: "Invalid email: not-an-email"

---

## ❌ Test Case 9: Customer Upload - Invalid Phone

### Test Data
```csv
name,email,phone,address,city,country
Short Phone,short@test.com,123,Address,City,USA
Long Phone,long@test.com,12345678901234567890,Address,City,USA
```

### Steps
1. Upload CSV with phone too short/long
2. Check results

### Expected Results
- ❌ Both rows fail with: "Invalid phone: ... (must be 10-15 digits)"

---

## ❌ Test Case 10: Invalid Status Value

### Test Data
```csv
name,sku,category,price,stock_quantity,reorder_level,description,status
Product,TEST-STATUS-001,Electronics,99.99,100,20,Test,unknown_status
```

### Steps
1. Upload CSV with invalid status
2. Check results

### Expected Results
- ❌ Row failed with: "Invalid status: unknown_status. Must be one of ['active', 'inactive', 'discontinued']"

---

## 🔧 Test Case 11: File Size Validation

### Steps
1. Create a CSV file > 5MB
2. Try to upload
3. Check form validation

### Expected Results
- ❌ Form error: "File size must be less than 5MB"
- ❌ File not uploaded

---

## 🔧 Test Case 12: File Type Validation

### Steps
1. Create/select an Excel (.xlsx) or text (.txt) file
2. Try to upload
3. Check form validation

### Expected Results
- ❌ Form error: "File must be a CSV file"
- ❌ File not uploaded

---

## ✅ Test Case 13: Sample CSV Download

### Steps
1. Navigate to `/products/bulk-upload/` or `/customers/bulk-upload/`
2. Click "Download Sample CSV" button

### Expected Results
- ✅ File downloads: `products_sample.csv` or `customers_sample.csv`
- ✅ File contains proper headers and 2 sample rows
- ✅ Format is exactly as required

---

## ✅ Test Case 14: Auto-Category Creation (Products)

### Test Data
```csv
name,sku,category,price,stock_quantity,reorder_level
Product in New Category,AUTO-CAT-001,Brand New Category,99.99,100,20
```

### Steps
1. Ensure "Brand New Category" doesn't exist
2. Upload CSV with new category
3. Check database

### Expected Results
- ✅ Product created successfully
- ✅ New category auto-created
- ✅ Go to Products list to verify

---

## ✅ Test Case 15: Navigation & UI

### Steps
1. Go to Products list page
2. Observe buttons in header

### Expected Results
- ✅ "Add New Product" button (primary)
- ✅ "Bulk Upload" button (success/green)
- ✅ "Low Stock" button (warning/yellow)
- ✅ Same for Customers page (without Low Stock)

---

## 🧮 Test Case 16: Large File (Performance)

### Steps
1. Create CSV with 1000 rows of valid data
2. Upload and time the process
3. Check results accuracy

### Expected Results
- ✅ All 1000 rows processed
- ✅ Correct success/failure counts
- ✅ Performance acceptable (< 30 seconds typical)
- ✅ All records created correctly

---

## 📊 Test Case 17: Mixed Success & Failure

### Test Data
```csv
name,sku,category,price,stock_quantity,reorder_level
Valid Product 1,MIX-001,Electronics,99.99,100,20
Invalid Price,-50.00,Electronics,MIX-002,100,20
Valid Product 2,MIX-003,Electronics,149.99,50,10
Missing Field,MIX-004,Electronics,199.99,,10
Valid Product 3,MIX-005,Electronics,249.99,75,15
```

### Steps
1. Upload CSV
2. Check results page

### Expected Results
- ⚠️ Summary: 3 Successful, 2 Failed (60% success rate)
- ✅ Success table shows 3 valid products
- ❌ Failure table shows 2 errors with reasons
- ⚠️ User can review and fix errors

---

## 🔐 Test Case 18: Authentication Required

### Steps
1. Log out
2. Try to access `/products/bulk-upload/`
3. Try to access `/customers/bulk-upload/`

### Expected Results
- 🔐 Redirected to login page
- 🔐 Cannot access bulk upload without authentication

---

## 📝 Testing Checklist

- [ ] Product upload - success scenario
- [ ] Customer upload - success scenario
- [ ] Missing headers error
- [ ] Duplicate SKU error
- [ ] Duplicate email error
- [ ] Invalid price validation
- [ ] Invalid stock validation
- [ ] Invalid email validation
- [ ] Invalid phone validation
- [ ] Invalid status error
- [ ] File size validation
- [ ] File type validation
- [ ] Sample CSV download
- [ ] Auto-category creation
- [ ] Navigation buttons visible
- [ ] Large file performance
- [ ] Mixed success & failure
- [ ] Authentication required

---

## 🚀 Performance Baseline

Expected times for CSV processing:
- 100 rows: < 1 second
- 500 rows: < 2 seconds
- 1000 rows: < 5 seconds
- 5000 rows: < 20 seconds

If performance is worse, consider implementing async processing.

---

## 🐛 Bug Report Template

If you find issues, note:
- [ ] Test case number
- [ ] CSV data used
- [ ] Expected vs actual result
- [ ] Error message (if any)
- [ ] Browser/OS details
- [ ] Steps to reproduce

---

**All tests complete? Feature is ready for production! ✅**
