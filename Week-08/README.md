# Week 8 — Customer Analytics

## Overview

Week 8 focuses on customer analytics and customer relationship behaviour within the Heavy Supplier, Inventory & Warehouse Analytics project.

The analysis uses the customer master data and sales order history to evaluate customer geographic behaviour, lifetime value, purchasing patterns, retention, churn risk, cohort behaviour, repeat purchasing and RFM-based segmentation.

## Data Sources

The following source datasets were used:

- `customers.csv`
- `sales_orders_header.csv`

### Dataset Validation

- Customer records: 500
- Unique customer IDs: 500
- Sales order records: 20,000
- Unique sales order IDs: 20,000
- Missing customer IDs in sales orders: 0
- Delivered orders: 18,033
- Customers with delivered orders: 500
- Order date range: 2019-01-01 to 2024-12-31

---

## Week 8 Analyses

### 1. Customer Geographic / Regional Behaviour Analysis

Analysed customer and revenue performance across six regions:

- South
- West
- East
- North
- Central
- North East

Key findings:

- South generated the highest regional revenue: 9,252,650,372.80
- South had the highest customer count: 158
- South achieved the highest regional performance score: 85.21
- North had the highest average customer revenue: 61,194,762.03
- North had the highest average orders per customer: 36.94
- Central and North East showed comparatively lower regional performance.

**Main output:**

`outputs/customer_geographic_regional_behaviour_analysis.csv`

---

### 2. Customer Lifetime Value (CLV) Analysis

Estimated customer lifetime value using historical purchasing behaviour.

Key findings:

- Total customer revenue: 29,253,993,162.40
- Total estimated CLV: 25,103,379,398.91
- Average estimated CLV: 50,206,758.80
- High / Very High Value customers: 250
- Very High Value customers: 125
- Highest CLV customer: C0153
- Highest estimated CLV: 90,809,349.33
- Highest average regional CLV: North
- Highest average customer-type CLV: Dealer

**Outputs:**

- `outputs/customer_lifetime_value_analysis.csv`
- `outputs/customer_lifetime_value_segment_summary.csv`
- `outputs/customer_lifetime_value_customer_type_summary.csv`
- `outputs/customer_lifetime_value_region_summary.csv`

---

### 3. Customer RFM Analysis & Segmentation

Performed Recency, Frequency and Monetary (RFM) analysis for all 500 customers.

Key segments:

- Champions: 68
- Loyal Customers: 52
- At-Risk Customers: 118
- Hibernating Customers: 82

Customer priority distribution:

- Critical Priority: 92
- High Priority: 117
- Medium Priority: 126
- Low Priority: 165

Highest monetary customer:

- Customer: C0153
- Revenue: 108,200,489.60
- Delivered orders: 56

**Outputs:**

- `outputs/customer_rfm_segmentation_analysis.csv`
- `outputs/customer_rfm_segment_summary.csv`

---

### 4. Customer Retention Analysis

Evaluated customer activity and retention status using purchase recency and customer purchasing behaviour.

Retention status:

- Active Customer: 167
- Recently Inactive: 218
- At Risk: 90
- Churn Risk: 25

Key findings:

- Customers requiring retention action: 115
- Overall active/recent retention: 77.0%
- Recently inactive customers represented 43.78% of revenue.
- Active customers represented 34.25% of revenue.

**Outputs:**

- `outputs/customer_retention_analysis.csv`
- `outputs/customer_retention_summary.csv`

---

### 5. Customer Churn Analysis

Evaluated customer churn risk and identified customers requiring retention intervention.

Churn status:

- Active Customer: 308
- At Risk: 125
- Churn Risk: 42
- Churned Customer: 25

Key findings:

- Customers requiring retention action: 192
- Customers requiring action: 38.4%
- Revenue at risk: 10,991,751,385.20

**Outputs:**

- `outputs/customer_churn_analysis.csv`
- `outputs/customer_churn_summary.csv`

---

### 6. Customer Cohort & Repeat Purchase Analysis

Analysed customer acquisition cohort, purchasing lifespan and repeat-purchase behaviour.

Key findings:

- All 500 customers belong to the 2019 first-purchase cohort.
- Total repeat customers: 500
- One-time customers: 0
- Repeat customer rate: 100.00%
- Average delivered orders per customer: 36.07

**Outputs:**

- `outputs/customer_cohort_repeat_purchase_analysis.csv`
- `outputs/customer_cohort_summary.csv`

---

### 7. Customer Purchase Frequency & Behaviour Analysis

Classified customers according to purchasing frequency and customer value.

Purchase frequency distribution:

- Very High Frequency: 52
- High Frequency: 76
- Medium Frequency: 307
- Low Frequency: 65

Key findings:

- High / Very High Frequency customers: 128
- Low-frequency high-value customers: 10
- Average orders per customer: 36.07
- Average order value: 1,622,908.50
- Highest frequency customer: C0153
- Highest frequency: 56 delivered orders

**Outputs:**

- `outputs/customer_purchase_frequency_behaviour_analysis.csv`
- `outputs/customer_purchase_frequency_summary.csv`
- `outputs/customer_purchase_frequency_customer_type_summary.csv`
- `outputs/customer_purchase_frequency_region_summary.csv`
- `outputs/customer_purchase_frequency_industry_summary.csv`

---

## Key Business Insights

The combined Week 8 customer analytics provide the following major insights:

1. **South is the leading region** by both customer count and total customer revenue.

2. **North demonstrates strong customer value**, recording the highest average customer revenue and highest average orders per customer.

3. **C0153 is the strongest customer** across several customer-value measures, including revenue, frequency and CLV.

4. **250 customers are High or Very High Value**, making customer-value protection an important business priority.

5. **68 customers are Champions** according to RFM segmentation and should receive proactive relationship management.

6. **192 customers require action under churn analysis**, representing 38.4% of the customer base.

7. **Revenue at risk is 10,991,751,385.20**, highlighting the financial importance of customer retention.

8. The dataset shows **100% repeat purchasing** among the 500 analysed customers.

9. **128 customers have High or Very High purchase frequency**, while 10 customers are classified as low-frequency but high-value customers.

10. **Central and North East require additional attention** because their regional performance scores are substantially lower than the leading regions.

---

## Recommended Business Actions

### Customer Retention

Prioritise customers classified as churn risk, at risk or churned for targeted retention and reactivation campaigns.

### High-Value Customer Management

Protect High Value and Very High Value customers through proactive relationship management and personalised offers.

### RFM-Based Targeting

Use Champions and Loyal Customers for retention and upselling while developing specific reactivation strategies for At-Risk and Hibernating customers.

### Regional Strategy

Maintain the strong performance of South and North while developing targeted growth strategies for Central and North East.

### Purchase Frequency Monitoring

Monitor changes in customer purchase frequency to identify early signs of declining engagement.

### Revenue-at-Risk Management

Use churn risk and customer value together to prioritise retention efforts toward customers where potential revenue loss is highest.

---

## Validation

All Week 8 customer-analysis outputs were validated.

Validation results:

- Duplicate customer IDs: 0
- Missing customer IDs: 0
- Missing values: 0
- Negative revenue values: 0
- Negative CLV values: 0
- Negative churn risk values: 0
- Negative retention scores: 0
- Main customer outputs contain 500 customer records.

---

## Documentation

Final customer insights are documented in:

`docs/week8_customer_insights.txt`

---

## Week 8 Deliverables

The Week 8 repository contains:

- Customer geographic / regional behaviour analysis
- Customer lifetime value analysis
- RFM analysis and segmentation
- Customer retention analysis
- Customer churn analysis
- Customer cohort and repeat-purchase analysis
- Customer purchase frequency and behaviour analysis
- CSV analytical outputs
- Summary outputs
- Customer insights documentation
- This README

---

## Week 8 Status

**Status: Completed**

All planned Week 8 customer analytics tasks, output generation and validation activities have been completed.