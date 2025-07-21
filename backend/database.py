from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///receipts.db")
SessionLocal = sessionmaker(bind=engine)

class Receipt(Base):
    __tablename__ = "receipts"
    id = Column(Integer, primary_key=True, index=True)
    item = Column(String)
    amount = Column(Float)

Base.metadata.create_all(bind=engine)

def save_to_db(data):
    session = SessionLocal()
    for item, amount in data:
        receipt = Receipt(item=item, amount=amount)
        session.add(receipt)
    session.commit()
    session.close()
