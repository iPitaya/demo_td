from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,Text,CHAR
from sqlalchemy import create_engine
from sqlalchemy.orm import (
	scoped_session,
	sessionmaker,
	)

SQLALCHEMY_CONF_URL = 'mysql+mysqldb://%s:%s@%s:%s/%s?charset=utf8' % ('root', '', '127.0.0.1', 3306, 'test')
engine = create_engine(SQLALCHEMY_CONF_URL,echo = False)
Base = declarative_base()
Session = scoped_session(sessionmaker(bind=engine))
session = Session()
#Base.metadata.bind = engine

class MyModel(Base):
	__tablename__ = 'pyach'
	id = Column(Integer,primary_key=True)
	name = Column(CHAR(8))
	value = Column(CHAR(10))
	def __init__(self,name,value):
		self.name = name
		self.value = value
	
	def __repr__(self):
		return "<Metadata('%s','%s')>" % (self.name,self.value)

if __name__ == "__main__":
	#Base.metadata.create_all(engine)
	#user = MyModel(name='qwe',value='sda')
	#session.add(user)
	session.commit()
	query = session.query(MyModel)
	for user in query:
		print user.name,user.value

