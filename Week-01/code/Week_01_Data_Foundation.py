# ============================================================
# HEAVY SUPPLIER & WAREHOUSE ANALYTICS
# WEEK 01 — DATA FOUNDATION & EXPLORATION
# ============================================================

import pandas as pd
import os

# ------------------------------------------------------------
# 1. SOURCE DATASETS
# ------------------------------------------------------------

DATA_PATH = r"D:\Educational Documents\Education documents\Courses + certification\virtual internship\HeavySuppliersWarehouseDatasets"

branches = pd.read_csv(os.path.join(DATA_PATH, "branches.csv"))
customers = pd.read_csv(os.path.join(DATA_PATH, "customers.csv"))
inventory = pd.read_csv(os.path.join(DATA_PATH, "inventory_master.csv"))
invoices = pd.read_csv(os.path.join(DATA_PATH, "invoices.csv"))
payments = pd.read_csv(os.path.join(DATA_PATH, "payments.csv"))
products = pd.read_csv(os.path.join(DATA_PATH, "products.csv"))
po_header = pd.read_csv(os.path.join(DATA_PATH, "purchase_orders_header.csv"))
po_lines = pd.read_csv(os.path.join(DATA_PATH, "purchase_orders_lines.csv"))
so_header = pd.read_csv(os.path.join(DATA_PATH, "sales_orders_header.csv"))
so_lines = pd.read_csv(os.path.join(DATA_PATH, "sales_orders_lines.csv"))
stock = pd.read_csv(os.path.join(DATA_PATH, "stock_ledger.csv"))
suppliers = pd.read_csv(os.path.join(DATA_PATH, "suppliers.csv"))

# ------------------------------------------------------------
# 2. DATA PROFILING
# ------------------------------------------------------------

dataframes = {
    "branches": branches,
    "customers": customers,
    "inventory_master": inventory,
    "invoices": invoices,
    "payments": payments,
    "products": products,
    "purchase_orders_header": po_header,
    "purchase_orders_lines": po_lines,
    "sales_orders_header": so_header,
    "sales_orders_lines": so_lines,
    "stock_ledger": stock,
    "suppliers": suppliers
}

print("DATASET OVERVIEW")
for name, data in dataframes.items():
    print(f"{name}: {data.shape[0]} rows × {data.shape[1]} columns")

# ------------------------------------------------------------
# 3. DUPLICATE ID CHECKS
# ------------------------------------------------------------

print("\nDUPLICATE ID CHECKS")

print("Products duplicate IDs:",
      products["product_id"].duplicated().sum())

print("Branches duplicate IDs:",
      branches["branch_id"].duplicated().sum())

print("Customers duplicate IDs:",
      customers["customer_id"].duplicated().sum())

print("Suppliers duplicate IDs:",
      suppliers["supplier_id"].duplicated().sum())

# ------------------------------------------------------------
# 4. INVENTORY PRODUCT-BRANCH VALIDATION
# ------------------------------------------------------------

print("\nINVENTORY VALIDATION")

print("Inventory rows:", len(inventory))
print(
    "Unique product-branch combinations:",
    inventory[["product_id", "branch_id"]].drop_duplicates().shape[0]
)

# ------------------------------------------------------------
# 5. REFERENTIAL INTEGRITY
# ------------------------------------------------------------

print("\nREFERENTIAL INTEGRITY CHECKS")

print(
    "Invalid PO supplier IDs:",
    (~po_header["supplier_id"].isin(suppliers["supplier_id"])).sum()
)

print(
    "Invalid PO branch IDs:",
    (~po_header["branch_id"].isin(branches["branch_id"])).sum()
)

print(
    "Invalid PO line product IDs:",
    (~po_lines["product_id"].isin(products["product_id"])).sum()
)

print(
    "Invalid SO customer IDs:",
    (~so_header["customer_id"].isin(customers["customer_id"])).sum()
)

print(
    "Invalid SO branch IDs:",
    (~so_header["branch_id"].isin(branches["branch_id"])).sum()
)

print(
    "Invalid SO line product IDs:",
    (~so_lines["product_id"].isin(products["product_id"])).sum()
)

print(
    "Invalid stock product IDs:",
    (~stock["product_id"].isin(products["product_id"])).sum()
)

print(
    "Invalid stock branch IDs:",
    (~stock["branch_id"].isin(branches["branch_id"])).sum()
)

print(
    "Invalid invoice SO IDs:",
    (~invoices["so_id"].isin(so_header["so_id"])).sum()
)

print(
    "Invalid invoice customer IDs:",
    (~invoices["customer_id"].isin(customers["customer_id"])).sum()
)

print(
    "Invalid payment invoice IDs:",
    (~payments["invoice_id"].isin(invoices["invoice_id"])).sum()
)

# ------------------------------------------------------------
# 6. DATA TYPE CONVERSION
# ------------------------------------------------------------

date_columns = [
    "order_date",
    "delivery_date"
]

for column in date_columns:
    if column in so_header.columns:
        so_header[column] = pd.to_datetime(
            so_header[column], errors="coerce"
        )

po_header["order_date"] = pd.to_datetime(
    po_header["order_date"], errors="coerce"
)

po_header["expected_delivery_date"] = pd.to_datetime(
    po_header["expected_delivery_date"], errors="coerce"
)

po_header["received_date"] = pd.to_datetime(
    po_header["received_date"], errors="coerce"
)

# ------------------------------------------------------------
# 7. PURCHASE DELIVERY ANALYSIS
# ------------------------------------------------------------

purchase_delivery = po_header.copy()

purchase_delivery["delivery_delay_days"] = (
    purchase_delivery["received_date"]
    - purchase_delivery["expected_delivery_date"]
).dt.days

purchase_delivery["delivery_status"] = "On Time"

purchase_delivery.loc[
    purchase_delivery["delivery_delay_days"] > 0,
    "delivery_status"
] = "Delayed"

print("\nPURCHASE DELIVERY")

print(
    purchase_delivery["delivery_status"].value_counts()
)

# ------------------------------------------------------------
# 8. DATA DICTIONARY
# ------------------------------------------------------------

data_dictionary = []

for table_name, data in dataframes.items():
    for column in data.columns:
        data_dictionary.append({
            "table": table_name,
            "column": column,
            "data_type": str(data[column].dtype),
            "missing_values": data[column].isna().sum(),
            "unique_values": data[column].nunique()
        })

data_dictionary = pd.DataFrame(data_dictionary)

print("\nTotal documented columns:", len(data_dictionary))

print(
    "Columns with missing values:",
    (data_dictionary["missing_values"] > 0).sum()
)

print(
    "Total missing values:",
    data_dictionary["missing_values"].sum()
)

# ------------------------------------------------------------
# 9. MISSING RECEIVED DATE VALIDATION
# ------------------------------------------------------------

missing_received = po_header[
    po_header["received_date"].isna()
]

print("\nMissing received dates:", len(missing_received))

print(
    missing_received["po_status"].value_counts(dropna=False)
)

# ------------------------------------------------------------
# 10. OUTPUT DIRECTORY
# ------------------------------------------------------------

OUTPUT_PATH = os.path.join(DATA_PATH, "Week-01")

os.makedirs(os.path.join(OUTPUT_PATH, "code"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_PATH, "data_dictionary"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_PATH, "outputs"), exist_ok=True)

data_dictionary.to_csv(
    os.path.join(
        OUTPUT_PATH,
        "data_dictionary",
        "data_dictionary.csv"
    ),
    index=False
)

print("\nWeek 01 data foundation script completed.")
