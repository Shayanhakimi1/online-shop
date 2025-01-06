from sqlalchemy import *
from  extensions import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Product(db.Model):
    __tablename__ = 'product'
    id: Mapped[int] = mapped_column(primary_key=True,index=True)
    name: Mapped[str] = mapped_column(unique=True,nullable=False,index=True)
    description: Mapped[str] = mapped_column(nullable=False, index=True)
    price: Mapped[int] = mapped_column(nullable=False,index=True)
