import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = 'mysql://{0}:{1}@{2}/{3}'.format(
    os.environ.get('MYSQL_USER', ''),
    os.environ.get('MYSQL_PASSWORD', ''),
    os.environ.get('MYSQL_HOST', 'localhost'),
    os.environ.get('MYSQL_DATABASE', '')
)
engine = create_engine(db_url, echo=True)
Session = sessionmaker(bind=engine)
