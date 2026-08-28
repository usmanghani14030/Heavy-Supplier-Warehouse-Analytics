# Week 6 — Core Warehouse Operations & Efficiency Analytics

## Sprint Overview

Week 6 focused on warehouse operations, product–warehouse alignment, warehouse performance, capacity utilisation, bottleneck detection, and benchmarking.

## Completed Analyses

### 1. Product–Warehouse Alignment
- Analysed product distribution across warehouses.
- Measured warehouse coverage, stock distribution and stock concentration.
- 30 products were analysed.
- All products had full warehouse coverage.
- All products were classified as having balanced stock distribution.

### 2. Warehouse Throughput Analysis
- Analysed order volume and units processed by warehouse.
- Calculated throughput efficiency using units per square foot.
- Kolkata East Depot recorded the highest throughput efficiency at 8.57 units/sqft.
- Delhi Central recorded the lowest at 4.53 units/sqft.

### 3. Warehouse Capacity Analysis
- Evaluated current stock against available warehouse capacity.
- Kolkata East Depot had the highest capacity pressure at 120.49%.
- Delhi Central had the lowest capacity pressure at 83.80%.
- 3 warehouses were classified as Normal, 2 as Low Pressure and 1 as High Pressure.

### 4. Warehouse Performance Scoring
- Combined throughput, order volume and capacity efficiency into an overall performance score.
- Chennai South Hub ranked first with a performance score of 77.20.
- Hyderabad Logistics ranked sixth with a score of 20.96.
- Performance classifications included High, Moderate, Low and Critical Performance.

### 5. Operational Bottleneck Detection
- Identified operational bottlenecks using warehouse performance and capacity indicators.
- 3 warehouses were identified with Capacity Bottlenecks.
- 2 warehouses were identified with Throughput Bottlenecks.
- 1 warehouse had No Major Bottleneck.
- Hyderabad Logistics was classified as Critical operational risk.

### 6. Warehouse Utilisation Benchmarking
- Benchmarked warehouse performance against the average warehouse metrics.
- Chennai South Hub was classified as an Efficient Benchmark.
- Kolkata East Depot and Ahmedabad West Hub showed high output with capacity concerns.
- Delhi Central and Pune Distribution were below benchmark.
- Hyderabad Logistics was below benchmark with a capacity concern.

### 7. Warehouse Space Utilisation
- Evaluated warehouse space utilisation and stock density.
- 3 warehouses were classified as Over Capacity.
- 1 warehouse was Near Capacity.
- 2 warehouses had Available Capacity.
- Kolkata East Depot recorded the highest utilisation at 120.49%.
- Delhi Central recorded the lowest at 83.80%.

## Key Business Insights

- Warehouse performance varies significantly across the network.
- Kolkata achieves the highest throughput efficiency but operates above capacity.
- Chennai provides the strongest overall warehouse performance while maintaining available capacity.
- Hyderabad requires the highest operational attention because of its critical performance classification and capacity pressure.
- Delhi has available capacity but comparatively low throughput efficiency.
- Capacity and throughput should therefore be evaluated together rather than independently.

## Deliverables

The following analytical outputs are included in this week's submission:

- product_warehouse_alignment_analysis.csv
- warehouse_throughput_analysis.csv
- warehouse_capacity_analysis.csv
- warehouse_performance_scoring.csv
- operational_bottleneck_analysis.csv
- warehouse_utilisation_benchmarking.csv
- warehouse_space_utilisation_analysis.csv

## Validation

All completed Week 6 outputs were validated for:
- Missing values
- Duplicate IDs
- Required columns
- Negative or invalid values
- Logical classification outputs

The validated analytical outputs are ready for submission.

## Tools & Methods

- Python
- Pandas
- NumPy
- CSV-based transactional datasets
- Descriptive analytics
- KPI benchmarking
- Ranking and scoring
- Capacity and utilisation analysis
- Operational risk classification

## Sprint Outcome

Week 6 successfully extended the project from product and inventory analytics into warehouse operations and efficiency analysis, producing portfolio-ready analytical outputs for warehouse decision-making.
