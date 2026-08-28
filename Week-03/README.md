# Week 03 — Inventory Risk & Demand Exploration

## Project
Heavy Supplier, Inventory & Warehouse Analytics

## Sprint Objective
Analyse inventory risk, product demand trends and stock movement activity to identify products requiring management attention and support better inventory planning.

## Analyses Completed

### 1. Overstock & Understock Detection
Analysed 180 inventory records across 30 products and 6 branches.

All 180 records were classified as Overstock based on the supplied maximum-stock thresholds.

### 2. Product Demand Trend Analysis
Analysed 72 months of sales data across 30 products.

Demand trends:
- 10 Decreasing
- 7 Strongly Decreasing
- 6 Strongly Increasing
- 3 Increasing
- 4 Stable

### 3. Movement-Based Inventory Aging
Used stock-ledger movement dates because the inventory master does not contain a direct stock-age field.

All 180 product-branch combinations had recorded movement within 30 days of the latest movement date in the dataset.

### 4. Inventory + Demand Risk Analysis

Products were classified into four combined risk groups:

- 7 High Risk — Overstock + Strong Demand Decline
- 11 Medium Risk — Overstock + Demand Decline
- 6 Growth Opportunity — Overstock + Rising Demand
- 6 Monitor — Overstock + Stable/Moderate Demand

## Key Business Insight

The analysis indicates a potential mismatch between inventory levels and demand.

All analysed inventory records were above their configured maximum stock levels, while 17 of 30 products showed declining demand.

This creates a potential working-capital and inventory-efficiency concern, particularly for products combining high inventory exposure with strongly declining demand.

## High-Risk Products

- P021 — Boom Cylinder BC-400
- P010 — Turbocharger TB-900
- P022 — Control Valve CV-75
- P023 — Idler Wheel IW-55
- P018 — Wheel Rim WR-24
- P016 — Radiator RD-250
- P017 — Fan Belt FB-30

## Deliverables

- `outputs/overstock_understock_analysis.csv`
- `outputs/product_demand_trend.csv`
- `outputs/product_demand_trend_summary.csv`
- `outputs/inventory_aging_analysis.csv`
- `outputs/inventory_demand_risk_analysis.csv`
- `docs/week3_insights.txt`

## Notes

Inventory aging in this sprint is movement-based rather than physical stock-age analysis. Recent stock movement does not necessarily mean the physical inventory was recently purchased.

## Sprint Status

Week-03 analysis and documentation completed.
