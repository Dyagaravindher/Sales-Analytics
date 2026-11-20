import pandas as pd
from sqlalchemy import func

from app.database import SessionLocal, engine, Base
from app.models import Sale

CSV_PATH = "data/processed/clean_sales.csv"

COLUMN_MAP = {
    "Order ID": "order_id",
    "Order Date": "order_date",
    "Ship Date": "ship_date",
    "Ship Mode": "ship_mode",
    "Customer ID": "customer_id",
    "Customer Name": "customer_name",
    "Segment": "segment",
    "Country": "country",
    "City": "city",
    "State": "state",
    "Postal Code": "postal_code",
    "Region": "region",
    "Product ID": "product_id",
    "Category": "category",
    "Sub-Category": "sub_category",
    "Product Name": "product_name",
    "Sales": "sales",
    "Year": "year",
    "Month": "month",
    "YearMonth": "year_month",
}


def load_data():
    Base.metadata.create_all(bind=engine)

    df = pd.read_csv(
        CSV_PATH,
        parse_dates=["Order Date", "Ship Date"],
        dtype={"Postal Code": str},
    )
    df = df.rename(columns=COLUMN_MAP)
    df = df[list(COLUMN_MAP.values())]
    df["order_date"] = df["order_date"].dt.date
    df["ship_date"] = df["ship_date"].dt.date

    records = df.to_dict(orient="records")

    db = SessionLocal()
    try:
        db.query(Sale).delete()
        db.bulk_insert_mappings(Sale, records)
        db.commit()

        count = db.query(func.count(Sale.id)).scalar()
        total = db.query(func.sum(Sale.sales)).scalar()
        print(f"Rows in CSV: {len(df)}")
        print(f"Rows in database: {count}")
        print(f"Total sales: {total:.2f}")
    finally:
        db.close()


if __name__ == "__main__":
    load_data()