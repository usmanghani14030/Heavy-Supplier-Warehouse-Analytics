# Heavy Supplier & Warehouse Analytics
## Week 01 — Data Foundation & Exploration

### 1. Project Overview

This project analyses heavy supplier, product, inventory, warehouse, customer and transactional data to support data-driven supply-chain decisions.

Week 01 focused on establishing a reliable data foundation through profiling, validation, integration, feature engineering and initial exploratory analytics.

### 2. Dataset Overview

The project contains 12 source datasets:

- branches
- customers
- inventory_master
- invoices
- payments
- products
- purchase_orders_header
- purchase_orders_lines
- sales_orders_header
- sales_orders_lines
- stock_ledger
- suppliers

### 3. Data Profiling

The source datasets were profiled for:

- Number of rows and columns
- Data types
- Missing values
- Unique values
- Duplicate identifiers
- Dataset relationships

A total of 134 source columns were documented.

### 4. Data Quality & Validation

Duplicate ID checks were performed for products, branches, customers and suppliers.

Referential integrity was also checked across purchase orders, sales orders, stock movements, invoices and payments.

No invalid foreign-key relationships were identified.

The only missing-value issue was found in purchase_orders_header.received_date.

There were 2,370 missing received dates. Validation confirmed that all 2,370 records belonged to Cancelled purchase orders, while all Received purchase orders had a received date. Therefore, the missing values were considered business-valid rather than a data integrity error.

### 5. Data Integration

The following analytical datasets were integrated:

- Sales transactions with products, customers and branches
- Purchase transactions with products and suppliers
- Inventory with products and branches
- Stock ledger with products and branches
- Financial invoices with payment information, customers and branches

All major integration checks showed zero missing product, customer, supplier or branch matches.

### 6. Initial Feature Engineering

Key analytical features were created for:

- Inventory value
- Inventory stock status
- Supplier delivery delay
- Supplier delivery performance
- Supplier contribution
- Supplier risk
- Customer purchase behaviour
- RFM metrics
- Customer segmentation

### 7. Initial Business Analytics

#### Inventory

Inventory levels were compared against reorder levels, safety stock and maximum stock levels to identify inventory health and potential overstock/understock conditions.

#### Supplier Analytics

Supplier performance was evaluated using:

- Total purchase value
- Purchase share
- Number of purchase orders
- On-time delivery percentage
- Average delivery delay
- Reliability score
- Supplier risk classification

#### Customer Analytics

Customer behaviour was analysed using:

- Total purchase value
- Total orders
- Total items purchased
- Recency
- Frequency
- Monetary value
- RFM scoring
- Customer segmentation

500 customers were successfully analysed and segmented.

### 8. RFM Segmentation

The resulting customer segments were:

- Potential / Regular
- Loyal Customers
- New / Potential Customers
- Low-Value / Inactive
- Champions
- At-Risk High-Value

The segmentation identified 58 Champions and 49 At-Risk High-Value customers.

### 9. Week 01 Deliverables

The following outputs were generated:

- data_dictionary.csv
- inventory_analysis.csv
- stock_analysis.csv
- supplier_performance.csv
- supplier_contribution.csv
- supplier_risk.csv
- customer_analysis_rfm.csv

### 10. Next Phase

The next phase will expand the analysis into product performance, fast/slow-moving products, inventory turnover, stock health, warehouse efficiency and additional supply-chain analytics.

---
Heavy Supplier & Warehouse Analytics | CadetX Applied Work Experience
