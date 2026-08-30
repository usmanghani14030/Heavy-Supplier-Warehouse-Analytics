# Week 6 — Sprint Notes

## Sprint Goal

Analyse warehouse operations and efficiency by evaluating product–warehouse alignment, throughput, capacity, performance, bottlenecks, utilisation, and space efficiency.

## Work Completed

### Product–Warehouse Alignment
- Analysed product distribution across warehouse locations.
- Evaluated warehouse coverage and stock concentration.
- 30 products analysed.
- All 30 products had Full Coverage.
- All 30 products had Balanced Distribution.

### Warehouse Throughput & Capacity
- Analysed warehouse order volume and units processed.
- Measured throughput efficiency in units per square foot.
- Evaluated warehouse capacity pressure and capacity classification.

### Warehouse Performance Scoring
- Combined throughput, order volume and capacity efficiency into an overall performance score.
- Ranked all six warehouses.
- Chennai South Hub ranked #1 with a score of 77.20.
- Hyderabad Logistics ranked #6 with a score of 20.96.

### Operational Bottleneck Detection
- Identified operational bottlenecks using performance and capacity indicators.
- 3 Capacity Bottlenecks identified.
- 2 Throughput Bottlenecks identified.
- 1 warehouse had No Major Bottleneck.
- Hyderabad Logistics was identified as Critical operational risk.

### Warehouse Utilisation Benchmarking
- Benchmarked warehouses against network-level average metrics.
- Chennai South Hub was classified as an Efficient Benchmark.
- Kolkata East Depot and Ahmedabad West Hub showed high output with capacity concerns.
- Delhi Central and Pune Distribution were below benchmark.
- Hyderabad Logistics was below benchmark with a capacity concern.

### Warehouse Space Utilisation
- Evaluated warehouse space utilisation and stock density.
- 3 warehouses were Over Capacity.
- 1 warehouse was Near Capacity.
- 2 warehouses had Available Capacity.
- Kolkata East Depot recorded the highest utilisation at 120.49%.
- Delhi Central recorded the lowest utilisation at 83.80%.

## Key Findings

1. Chennai South Hub achieved the strongest overall warehouse performance.
2. Kolkata East Depot had the highest throughput efficiency but also the highest capacity pressure.
3. Hyderabad Logistics showed the weakest overall performance and was classified as Critical operational risk.
4. Delhi Central had available capacity but the lowest throughput efficiency.
5. Capacity pressure is concentrated in Kolkata, Ahmedabad and Hyderabad.
6. Strong output does not always indicate efficient capacity utilisation.

## Validation

All Week 6 analytical outputs were validated for:
- Missing values
- Duplicate branch/product IDs
- Required columns
- Negative or invalid numerical values
- Performance score limits
- Capacity and utilisation classifications

All completed validations passed successfully.

## Week 6 Deliverables

- product_warehouse_alignment_analysis.csv
- warehouse_throughput_analysis.csv
- warehouse_capacity_analysis.csv
- warehouse_performance_scoring.csv
- operational_bottleneck_analysis.csv
- warehouse_utilisation_benchmarking.csv
- warehouse_space_utilisation_analysis.csv
- README.md
- SPRINT_NOTES.md

## Tools Used

- Python
- Pandas
- NumPy
- CSV transactional datasets
- Descriptive analytics
- Benchmarking
- KPI scoring
- Capacity analysis
- Operational risk classification

## Sprint Outcome

Week 6 successfully delivered the warehouse operations and efficiency analytics layer of the Heavy Supplier, Inventory & Warehouse Analytics project. The outputs are validated and prepared for GitHub submission.
