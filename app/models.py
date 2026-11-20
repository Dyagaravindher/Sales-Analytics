from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String, index=True)
    order_date = Column(Date, index=True)
    ship_date = Column(Date)
    ship_mode = Column(String)
    customer_id = Column(String, index=True)
    customer_name = Column(String)
    segment = Column(String)
    country = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    region = Column(String, index=True)
    product_id = Column(String)
    category = Column(String, index=True)
    sub_category = Column(String)
    product_name = Column(String)
    sales = Column(Float)
    year = Column(Integer)
    month = Column(Integer)
    year_month = Column(String)