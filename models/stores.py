from models.base import Base
from sqlalchemy import ForeignKey, Index
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Stores(Base):
    __tablename__ = "stores"

    id: Mapped[int] = mapped_column(primary_key=True)
    store_id: Mapped[str] = mapped_column(unique=True)
    country: Mapped[int] = mapped_column(ForeignKey("countries.id"))
    name: Mapped[str]
    display_name: Mapped[str]
    second_hand_page_link: Mapped[str]