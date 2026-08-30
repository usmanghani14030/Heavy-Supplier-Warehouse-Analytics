# Week 9 — Supplier & Procurement Analytics

## Overview

Week 9 focuses on supplier performance, procurement risk, supplier concentration, purchasing cost, supplier-product relationships, and strategic sourcing analysis.

The objective is to evaluate supplier performance and identify procurement risks, cost opportunities, supplier dependencies, and strategic sourcing priorities.

## Analyses Completed

### 1. Supplier Performance Analysis
- Supplier purchase order activity
- Total ordered quantity
- Total purchase value
- Supplier performance classification

### 2. Supplier Delivery & Lead-Time Analysis
- Average supplier lead time
- Delivery variance
- On-time delivery rate
- Late delivery rate
- Supplier delivery risk classification

### 3. Supplier Quality & Procurement Risk Analysis
- Supplier quality indicators
- Delivery risk
- Lead-time risk
- Procurement risk score
- Supplier quality classification
- Procurement priority classification

### 4. Supplier Procurement Spend & Cost Analysis
- Total procurement spend
- Average purchase order value
- Supplier spend share
- PO share
- Cost efficiency classification
- Potential cost savings

### 5. Supplier Concentration & Dependency Analysis
- Top supplier spend concentration
- Top 3 and Top 5 supplier concentration
- Supplier HHI
- Effective supplier count
- Supplier dependency score
- Concentration risk

### 6. Supplier Pricing & Purchase Cost Analysis
- Average and median purchase cost
- Supplier cost variability
- Cost efficiency
- Procurement cost priority
- Potential supplier cost savings

### 7. Supplier Product Procurement Analysis
- Supplier-product relationships
- Procurement quantities
- Procurement values
- Product dependency
- Supplier share of product procurement
- Unit procurement cost
- Cost variance
- Supplier-product priority

### 8. Overall Supplier Performance & Risk Scorecard
- Performance score
- Delivery score
- Quality score
- Risk score
- Cost efficiency score
- Dependency score
- Overall supplier score
- Supplier ranking
- Supplier priority

### 9. Supplier Segmentation & Strategic Sourcing
- Strategic importance
- Supplier value
- Risk exposure
- Supplier segmentation
- Recommended sourcing strategy
- Diversification priority
- Negotiation priority
- Strategic sourcing priority

## Key Findings

- 8 suppliers were analysed across the procurement dataset.
- Total procurement spend analysed: approximately 346.62 billion.
- Supplier concentration was classified as low based on the calculated HHI.
- Despite low concentration, overall supplier dependency was classified as high.
- SUP0005 had the highest procurement spend and highest sourcing priority.
- SUP0006 achieved the highest overall supplier score of 78.36.
- SUP0004 had the lowest overall supplier score of 46.33.
- SUP0005 had the highest procurement risk score of 63.5.
- SUP0001 had the highest average purchase order cost.
- Estimated potential procurement cost savings were approximately 1.93 billion.
- SUP0006 was identified as a Strategic Partner.
- SUP0007 was identified as a Preferred Supplier.
- 5 suppliers were identified as requiring diversification attention.
- 3 suppliers were identified as requiring negotiation attention.

## Dataset Used

- suppliers.csv
- purchase_orders_header.csv
- purchase_orders_lines.csv
- products.csv

## Output Directory

All Week 9 analytical outputs are stored in:

`outputs/`

Final supplier insights are stored in:

`docs/week9_supplier_insights.txt`

## Validation

All Week 9 analyses were validated for:

- Duplicate supplier IDs
- Missing supplier IDs
- Missing values
- Negative procurement values
- Negative scores
- Score ranges
- Supplier-product duplicates
- Procurement spend share consistency

## Conclusion

Week 9 provides a comprehensive supplier and procurement analytics layer covering supplier performance, delivery, quality, risk, cost, concentration, dependency, supplier-product relationships, and strategic sourcing.

The analysis supports procurement decision-making by identifying high-value suppliers, supplier risks, cost-saving opportunities, diversification requirements, and strategic supplier relationships.
