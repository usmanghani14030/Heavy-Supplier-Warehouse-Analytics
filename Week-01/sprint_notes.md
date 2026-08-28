# Sprint 01 — Data Foundation & Exploration

## Sprint Goal

Establish a reliable data foundation for the Heavy Supplier & Warehouse Analytics project by profiling, validating, integrating and documenting the available datasets.

## Completed Tasks

- Profiled all 12 source datasets.
- Documented 134 source columns.
- Checked duplicate primary identifiers.
- Validated foreign-key relationships across datasets.
- Integrated sales data with product, customer and branch information.
- Integrated purchase data with product and supplier information.
- Integrated inventory and stock data with product and branch information.
- Integrated invoice and payment data.
- Created inventory analysis features.
- Created supplier delivery, performance, contribution and risk analysis.
- Created customer purchase behaviour analysis.
- Performed RFM analysis and customer segmentation.
- Created the initial data dictionary.
- Validated missing values and data consistency.
- Saved analytical outputs for the sprint.

## Data Quality Findings

There were no duplicate IDs in the main master datasets.

No invalid product, customer, supplier, branch, sales-order, purchase-order, invoice or payment relationships were identified.

The only missing-value issue was found in `purchase_orders_header.received_date`.

A total of 2,370 received dates were missing. All 2,370 belonged to Cancelled purchase orders. All Received purchase orders had a received date, so the missing values were considered business-valid.

## Key Initial Findings

### Inventory

All 180 product-branch inventory combinations were analysed.

Current stock levels were compared with reorder level, safety stock and maximum stock level to assess inventory health.

### Supplier

Supplier delivery performance was analysed using on-time delivery percentage and average delivery delay.

Supplier purchase contribution and risk were also assessed.

### Customer

500 customers were analysed using purchase value, order frequency and purchase recency.

RFM scoring produced six customer segments:

- Potential / Regular
- Loyal Customers
- New / Potential Customers
- Low-Value / Inactive
- Champions
- At-Risk High-Value

58 customers were classified as Champions and 49 as At-Risk High-Value.

## Sprint Deliverables

- README.md
- data_dictionary.csv
- inventory_analysis.csv
- stock_analysis.csv
- supplier_performance.csv
- supplier_contribution.csv
- supplier_risk.csv
- customer_analysis_rfm.csv

## Sprint Status

Status: COMPLETED

## Next Sprint Focus

The next sprint will focus on Product & Inventory Analytics, including:

- Product performance analysis
- Fast-moving product identification
- Slow-moving and dead stock analysis
- Inventory turnover
- Stock health
- ABC / Pareto classification
- Overstock and understock analysis
