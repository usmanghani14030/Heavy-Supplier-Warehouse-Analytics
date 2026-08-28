# Week 04 — Product, Inventory & Warehouse Analytics

## Project
Heavy Supplier, Inventory & Warehouse Analytics

## Objective

Week 04 focuses on warehouse capacity, space utilisation, product-warehouse alignment, warehouse performance, and bottleneck identification.

The analysis evaluates how inventory is distributed across warehouses and identifies locations that may require operational attention.

## Dataset Scope

- Branches: 6
- Products: 30
- Inventory records: 180
- Product-branch combinations: 180

### Warehouses

| Branch Code | Warehouse |
|---|---|
| DEL001 | Delhi Central |
| PUN001 | Pune Distribution |
| CHN001 | Chennai South Hub |
| HYD001 | Hyderabad Logistics |
| KOL001 | Kolkata East Depot |
| AHM001 | Ahmedabad West Hub |

## Analysis Outputs

The following analyses were completed:

1. `outputs/warehouse_space_utilisation.csv`
2. `outputs/warehouse_capacity_analysis.csv`
3. `outputs/product_warehouse_alignment.csv`
4. `outputs/warehouse_product_concentration.csv`
5. `outputs/warehouse_performance_scorecard.csv`
6. `outputs/warehouse_bottleneck_analysis.csv`

Detailed findings are documented in:

`docs/week4_insights.txt`

## Key Findings

### Warehouse Space Utilisation

All 6 warehouses were classified as **Over Capacity** based on the analytical utilisation calculation.

| Rank | Warehouse | Utilisation |
|---|---|---:|
| 1 | Kolkata | 19,061.17% |
| 2 | Ahmedabad | 16,993.93% |
| 3 | Hyderabad | 16,588.58% |
| 4 | Pune | 15,451.64% |
| 5 | Chennai | 14,509.89% |
| 6 | Delhi | 13,272.94% |

### Important Data Limitation

The dataset does not provide rack height, pallet configuration, aisle space, stacking rules, or an actual warehouse layout.

Therefore, the calculated utilisation percentages should be interpreted as **analytical capacity indicators rather than literal physical occupancy measurements**.

### Capacity Risk

All 6 warehouses were classified as **Critical** capacity risk.

### Product-Warehouse Alignment

All 6 warehouses store all 30 products.

The heaviest products identified were:

| Product | Description | Weight |
|---|---|---:|
| P015 | Engine Block EB-600 | 320 kg |
| P014 | Transmission Assembly TA-800 | 260 kg |
| P004 | Track Chain TC-45 | 210 kg |

### Warehouse Inventory Highlights

- **Chennai** recorded the highest inventory value at approximately **47.8B**.
- **Chennai** also recorded the highest stock weight at approximately **121.8M kg**.
- **Delhi** recorded the highest total stock quantity at approximately **3.29M units**.

## Warehouse Performance Scorecard

The overall warehouse performance ranking was:

| Rank | Warehouse | Score |
|---|---|---:|
| 1 | Delhi | 98.51 |
| 2 | Chennai | 94.42 |
| 3 | Pune | 94.00 |
| 4 | Hyderabad | 88.08 |
| 5 | Ahmedabad | 85.73 |
| 6 | Kolkata | 85.52 |

All warehouses were classified as **High Performance** under the applied performance model.

### Performance Model

The warehouse performance score was based on:

- Cost efficiency — 30%
- Employee productivity — 25%
- Market demand — 20%
- Capacity efficiency — 25%

## Warehouse Bottleneck Analysis

| Rank | Warehouse | Bottleneck Score | Classification |
|---|---|---:|---|
| 1 | Kolkata | 99.37 | Critical Bottleneck |
| 2 | Hyderabad | 90.53 | Critical Bottleneck |
| 3 | Ahmedabad | 86.60 | Critical Bottleneck |
| 4 | Pune | 78.99 | High Bottleneck Risk |
| 5 | Chennai | 74.49 | High Bottleneck Risk |
| 6 | Delhi | 69.19 | High Bottleneck Risk |

### Bottleneck Summary

- Critical: 3 warehouses
- High: 3 warehouses
- Moderate: 0 warehouses
- Low: 0 warehouses

## Key Business Insight

Warehouse performance and physical capacity pressure are separate operational dimensions.

**Delhi** ranked #1 in overall warehouse performance but #6 in bottleneck risk, indicating strong operational/financial efficiency despite comparatively lower bottleneck pressure.

In contrast, **Kolkata** ranked #6 in overall performance but #1 in bottleneck risk, indicating that it requires greater operational attention despite being evaluated across the same warehouse network.

This demonstrates why warehouse decision-making should not rely on a single performance metric.

## Conclusion

Week 04 identifies significant capacity and bottleneck pressure across the warehouse network while also showing differences in operational performance between locations.

The results can support future analysis of inventory allocation, warehouse optimisation, supplier flows, customer demand, and operational risk.

## Files

### Outputs
- `warehouse_space_utilisation.csv`
- `warehouse_capacity_analysis.csv`
- `product_warehouse_alignment.csv`
- `warehouse_product_concentration.csv`
- `warehouse_performance_scorecard.csv`
- `warehouse_bottleneck_analysis.csv`

### Documentation
- `docs/week4_insights.txt`
