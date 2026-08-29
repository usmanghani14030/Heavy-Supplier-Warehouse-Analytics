# Week 7 - Supplier, Procurement & Sourcing Analytics

## Overview

Week 7 focuses on supplier and procurement analytics for evaluating
supplier cost performance, procurement efficiency, supplier dependency,
procurement risk, delivery risk, sourcing diversification, and overall
supplier performance.

The analysis uses supplier master data, purchase order headers, and
purchase order line-level data.

---

## Dataset Coverage

- Suppliers analysed: 8
- Purchase orders: 24,000
- Received purchase orders: 21,630
- Cancelled purchase orders: 2,370

### Source Files

- `suppliers.csv`
- `purchase_orders_header.csv`
- `purchase_orders_lines.csv`

---

## Analyses Completed

### 1. Supplier Cost / Pricing Analysis

Evaluated supplier purchasing costs using weighted average unit cost,
purchase value share, and weighted cost variance.

Key observations:

- Weighted cost variance ranged from approximately 5.92% to 6.32%.
- Guangzhou Local Vendor Supplies had the highest weighted cost variance
  at approximately 6.32%.
- Hangzhou OEM Supplies had the lowest weighted cost variance at
  approximately 5.92%.

Output:

`outputs/supplier_cost_analysis.csv`

---

### 2. Supplier Concentration / Dependency Analysis

Evaluated purchasing concentration and supplier dependency based on
purchase value.

Key findings:

- Total purchase value: 346,621,977,539.14
- Top supplier share: 12.91%
- Top 3 supplier share: 38.10%
- Top 5 supplier share: 63.22%
- All 8 suppliers: Moderate Dependency
- Overall concentration assessment: Diversified

Output:

`outputs/supplier_concentration_dependency_analysis.csv`

---

### 3. Supplier Procurement Efficiency Analysis

Evaluated supplier performance using received and cancelled purchase
orders and procurement efficiency metrics.

Key findings:

- Average procurement efficiency score: 90.12
- Highest score: 90.59
- Lowest score: 89.72
- Excellent Procurement Efficiency: 5 suppliers
- Good Procurement Efficiency: 3 suppliers

Qingdao Distributor Supplies achieved the highest procurement
efficiency score of 90.59%.

Output:

`outputs/supplier_procurement_efficiency_analysis.csv`

---

### 4. Supplier Procurement Risk Analysis

Evaluated procurement risk using supplier lead time, reliability,
purchase order cancellation rate, import duty exposure, and purchasing
share.

Key findings:

- Average procurement risk score: 69.50
- Highest risk score: 84.46
- Lowest risk score: 54.93
- High Risk suppliers: 4
- Moderate Risk suppliers: 4

Highest-risk suppliers included:

1. Tianjin OEM Supplies - 84.46
2. Ningbo Distributor Supplies - 81.44
3. Qingdao Distributor Supplies - 81.39
4. Hangzhou OEM Supplies - 70.30

Output:

`outputs/supplier_procurement_risk_analysis.csv`

---

### 5. Supplier Lead-Time / Delivery Risk Analysis

Evaluated actual supplier delivery performance against expected delivery
dates.

Key findings:

- Received POs analysed: 21,630
- Overall on-time delivery rate: 84.90%
- Average delivery risk score: 42.75
- Highest delivery risk score: 61.30
- Lowest delivery risk score: 28.25
- All 8 suppliers: Moderate Delivery Risk

Tianjin OEM Supplies had the highest delivery risk score, followed by
Hangzhou OEM Supplies and Ningbo Distributor Supplies.

Output:

`outputs/supplier_lead_time_delivery_risk_analysis.csv`

---

### 6. Supplier Diversification / Sourcing Analysis

Evaluated supplier diversity by supplier type, region, purchase value,
and purchase order share.

Supplier type distribution:

- OEM: 3
- Distributor: 3
- Local Vendor: 2

Regional distribution:

- East China: 5
- South China: 2
- North China: 1

Key findings:

- Top supplier purchase share: 12.91%
- Top 3 supplier purchase share: 38.10%
- Top 5 supplier purchase share: 63.22%
- Overall sourcing classification: Diversified
- All suppliers: Moderate Dependency

East China represents the largest regional concentration and should
continue to be monitored.

Output:

`outputs/supplier_diversification_sourcing_analysis.csv`

---

### 7. Supplier Performance Scorecard

Combined supplier cost, procurement efficiency, procurement risk,
delivery performance, and supplier characteristics into an overall
supplier performance scorecard.

Key findings:

- Average performance score: 71.56
- Highest performance score: 74.30
- Lowest performance score: 68.85
- Good Supplier Performance: 5
- Moderate Supplier Performance: 3

### Top Suppliers

| Rank | Supplier | Score | Class |
|---|---|---:|---|
| 1 | Shenzhen OEM Supplies | 74.30 | Good |
| 2 | Guangzhou Local Vendor Supplies | 74.07 | Good |
| 3 | Suzhou Local Vendor Supplies | 73.48 | Good |
| 4 | Shanghai Distributor Supplies | 71.70 | Good |
| 5 | Hangzhou OEM Supplies | 71.45 | Good |
| 6 | Qingdao Distributor Supplies | 69.51 | Moderate |
| 7 | Ningbo Distributor Supplies | 69.12 | Moderate |
| 8 | Tianjin OEM Supplies | 68.85 | Moderate |

Output:

`outputs/supplier_performance_scorecard.csv`

---

## Key Business Insights

1. Supplier purchasing is broadly diversified, with no single supplier
   accounting for a dominant share of total purchasing value.

2. Procurement efficiency is strong across the supplier base, with an
   average score above 90.

3. Procurement risk is more significant than procurement efficiency,
   with four suppliers classified as High Risk.

4. Long supplier lead times contribute significantly to procurement and
   delivery risk.

5. Overall on-time delivery performance is 84.90%, indicating that
   delivery reliability should continue to be monitored.

6. Tianjin OEM Supplies represents the highest procurement and delivery
   risk and should receive priority monitoring.

7. East China contains five of the eight suppliers, creating a
   geographic concentration that should be considered in sourcing
   strategy.

8. Supplier performance scores range from 68.85 to 74.30, indicating
   relatively close overall supplier performance.

---

## Business Recommendations

- Maintain alternative sourcing options for critical products.
- Prioritize risk mitigation for high-risk suppliers.
- Closely monitor suppliers with long lead times.
- Reduce purchase order cancellation rates.
- Review supplier pricing where cost variance is relatively high.
- Continue monitoring geographic sourcing concentration.
- Use the supplier performance scorecard for regular supplier reviews.
- Establish periodic supplier risk and performance monitoring.

---

## Validation

All Week 7 analytical outputs passed final validation.

Validation checks included:

- Missing values
- Duplicate supplier IDs
- Required columns
- Negative and invalid values
- Purchase order count consistency
- Procurement rate consistency
- Delivery rate consistency
- Purchase share consistency
- Supplier ranking consistency
- Cumulative purchase share consistency
- Supplier performance ranking consistency

### Validation Status

**ALL WEEK 7 ANALYSES: PASS**

---

## Outputs

The following analytical outputs were generated:

1. `supplier_cost_analysis.csv`
2. `supplier_concentration_dependency_analysis.csv`
3. `supplier_procurement_efficiency_analysis.csv`
4. `supplier_procurement_risk_analysis.csv`
5. `supplier_lead_time_delivery_risk_analysis.csv`
6. `supplier_diversification_sourcing_analysis.csv`
7. `supplier_performance_scorecard.csv`

Documentation:

- `docs/week7_insights.txt`

---

## Conclusion

Week 7 provides a consolidated supplier and procurement performance
assessment.

The supplier base is broadly diversified and procurement efficiency is
strong. However, procurement risk, supplier lead times, cancellation
rates, and geographic concentration require continued monitoring.

The supplier performance scorecard provides a consolidated framework
for identifying suppliers that require monitoring, risk mitigation,
pricing review, or sourcing diversification.
