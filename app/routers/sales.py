from fastapi import APIRouter, Depends, Query
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Sale

router = APIRouter(tags=["Sales"])


@router.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    total_sales, total_orders, avg_sale, first_date, last_date = db.query(
        func.sum(Sale.sales),
        func.count(func.distinct(Sale.order_id)),
        func.avg(Sale.sales),
        func.min(Sale.order_date),
        func.max(Sale.order_date),
    ).one()

    return {
        "total_sales": round(total_sales, 2),
        "total_orders": total_orders,
        "average_sale_per_row": round(avg_sale, 2),
        "first_order_date": first_date,
        "last_order_date": last_date,
    }


@router.get("/monthly-sales")
def monthly_sales(db: Session = Depends(get_db)):
    rows = (
        db.query(Sale.year_month, func.sum(Sale.sales))
        .group_by(Sale.year_month)
        .order_by(Sale.year_month)
        .all()
    )
    return [{"month": month, "total_sales": round(total, 2)} for month, total in rows]


@router.get("/top-products")
def top_products(
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
):
    total = func.sum(Sale.sales).label("total_sales")
    rows = (
        db.query(Sale.product_name, total)
        .group_by(Sale.product_name)
        .order_by(total.desc())
        .limit(limit)
        .all()
    )
    return [{"product_name": name, "total_sales": round(amount, 2)} for name, amount in rows]


@router.get("/sales-by-region")
def sales_by_region(db: Session = Depends(get_db)):
    total = func.sum(Sale.sales).label("total_sales")
    rows = (
        db.query(Sale.region, total)
        .group_by(Sale.region)
        .order_by(total.desc())
        .all()
    )
    return [{"region": region, "total_sales": round(amount, 2)} for region, amount in rows]


@router.get("/sales-by-category")
def sales_by_category(db: Session = Depends(get_db)):
    total = func.sum(Sale.sales).label("total_sales")
    rows = (
        db.query(Sale.category, total)
        .group_by(Sale.category)
        .order_by(total.desc())
        .all()
    )
    return [{"category": category, "total_sales": round(amount, 2)} for category, amount in rows]


@router.get("/yearly-sales")
def yearly_sales(db: Session = Depends(get_db)):
    rows = (
        db.query(Sale.year, func.sum(Sale.sales))
        .group_by(Sale.year)
        .order_by(Sale.year)
        .all()
    )
    return [{"year": year, "total_sales": round(amount, 2)} for year, amount in rows]


@router.get("/sales")
def list_sales(
    region: str | None = None,
    category: str | None = None,
    year: int | None = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    query = db.query(Sale)

    if region:
        query = query.filter(Sale.region == region)
    if category:
        query = query.filter(Sale.category == category)
    if year:
        query = query.filter(Sale.year == year)

    total_rows = query.count()
    rows = query.order_by(Sale.order_date, Sale.id).offset(skip).limit(limit).all()

    return {
        "total_matching_rows": total_rows,
        "skip": skip,
        "limit": limit,
        "results": [
            {
                "order_id": r.order_id,
                "order_date": r.order_date,
                "customer_name": r.customer_name,
                "region": r.region,
                "category": r.category,
                "product_name": r.product_name,
                "sales": r.sales,
            }
            for r in rows
        ],
    }