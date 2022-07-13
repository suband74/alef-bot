from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Locality(Base):
    __tablename__ = "locality"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    reference = Column(String, nullable=False)
    population_size = Column(Integer)
    __table_args__ =  (UniqueConstraint('name', 'reference', name='loc_ref'),
    )
