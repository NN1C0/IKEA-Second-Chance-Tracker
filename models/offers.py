from models.base import Base
from sqlalchemy import ForeignKey, Index
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Offers(Base):
    __tablename__ = "offers"

    id: Mapped[int] = mapped_column(primary_key=True)
    store_id: Mapped[str] = mapped_column(ForeignKey("stores.id"))
    title: Mapped[str]
    description: Mapped[str]
    price: Mapped[float]
    article_price: Mapped[float]
    currency: Mapped[str]
    reason_discount: Mapped[str]
    hero_image: Mapped[str]