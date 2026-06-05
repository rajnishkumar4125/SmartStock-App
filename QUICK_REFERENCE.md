# Quick Reference - Bulk Upload Feature

## 🎯 Quick Access

### Product Upload
- **Form**: `http://localhost:8000/products/bulk-upload/`
- **Results**: Automatically shown after upload
- **Sample CSV**: Download from form page

### Customer Upload
- **Form**: `http://localhost:8000/customers/bulk-upload/`
- **Results**: Automatically shown after upload
- **Sample CSV**: Download from form page

---

## 📋 CSV Format Cheat Sheet

### Products (Required columns minimum)
```csv
name,sku,category,price,stock_quantity,reorder_level
Product Name,SKU-001,Category Name,99.99,100,20
```

### Customers (Required columns minimum)
```csv
name,email,phone,address,city,country
John Doe,john@example.com,9876543210,123 Street,City,Country
```

---

## ✅ Pre-Upload Checklist

- [ ] File is .CSV format
- [ ] File size is under 5MB
- [ ] All required columns are present
- [ ] No duplicate SKUs (products) or emails (customers)
- [ ] Data types are correct (numbers, valid emails, etc.)
- [ ] Phone numbers are 10-15 digits
- [ ] No extra spaces or special characters

---

## 🔍 Understanding Results

| Metric | What It Means |
|--------|---------------|
| **Total Processed** | Total rows in your CSV file |
| **Successful** | Records created successfully |
| **Failed** | Records that had errors |
| **Success Rate %** | Percentage of successful imports |

---

## ⚡ Common Commands

### Access Points from List Pages
1. Go to Products or Customers page
2. Click **"Bulk Upload"** button (green button with upload icon)
3. Click **"Download Sample CSV"** for template

---

## 🆘 Troubleshooting Quick Tips

| Problem | Check |
|---------|-------|
| File not accepted | Is it .CSV? Is it under 5MB? |
| Missing columns error | Do headers match exactly? |
| Duplicate error | Are SKU/email unique? |
| Invalid data error | Check format (numbers, emails, phone) |
| Still stuck? | Read BULK_UPLOAD_GUIDE.md |

---

## 📁 Key Files for Reference

| File | Purpose |
|------|---------|
| `CSV_UPLOAD_FLOWCHART.md` | Process flow & detailed rules |
| `BULK_UPLOAD_GUIDE.md` | User-friendly guide |
| `IMPLEMENTATION_SUMMARY.md` | Technical details |
| `core/utils/csv_handler.py` | Processing logic |

---

## 🚀 Typical Workflow

1. **Prepare Data** → Excel/CSV with correct format
2. **Download Sample** → Get template from form
3. **Upload File** → Select & upload CSV
4. **Review Results** → Check statistics & errors
5. **Fix & Retry** → If needed, correct & re-upload
6. **Verify** → Go to list to confirm records

---

## 💡 Pro Tips

✅ Test with 5-10 rows first to verify format  
✅ Use downloaded sample as template  
✅ Keep batch sizes under 1000 rows for speed  
✅ Review failed rows carefully  
✅ Fix duplicates before re-uploading  

---

## 📞 Need Help?

1. Check error message on results page
2. Review BULK_UPLOAD_GUIDE.md troubleshooting section
3. Verify CSV format with sample file
4. Check data validation rules in CSV_UPLOAD_FLOWCHART.md

---

**Ready to import bulk data?** 🚀  
Start with: Products → Bulk Upload (or Customers → Bulk Upload)
