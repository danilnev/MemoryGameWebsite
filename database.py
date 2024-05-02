from sqlalchemy.orm import sessionmaker
from models import engine, Base

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
