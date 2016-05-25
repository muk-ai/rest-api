import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = 'mysql://{0}:{1}@{2}/{3}'.format(
    os.environ['MYSQL_USER'],
    os.environ['MYSQL_PASSWORD'],
    os.environ['MYSQL_HOST'],
    os.environ['MYSQL_DATABASE']
)
engine = create_engine(db_url, echo=True)
Session = sessionmaker(bind=engine)
