from sqlmodel import SQLModel, Field
import datetime
from typing import Optional


class Orders(SQLModel, table=True):
    invoice_no: Optional[int] = Field(default=None, primary_key=True)
    stock_code: str
    description: str
    quantity: int
    invoice_date: datetime.datetime
    unit_price: float
    cust_id: int
    
