from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey
# import pymysql
# pymysql.install_as_MySQLdb()



# SQLite 连接engin方式
engine = create_engine('sqlite:///test1.db', echo=True)
metadata = MetaData(engine)

conn = engine.connect()

# MYSQL连接engin方式
# engine = create_engine('mysql+mysqldb://root:zz168601ZZ@localhost/test', echo=True)
# metadata = MetaData(engine)

def initDB():
        user_table = Table('user', metadata,
                           Column('id', Integer, primary_key=True),
                           Column('time', String(50)),
                           Column('ip', String(50)),
                           )

        address_table = Table('address', metadata,
                              Column('id', Integer, primary_key=True),
                              Column('user_id', None, ForeignKey('user.id')),
                              Column('email', String(128), nullable=False)
                              )

        metadata.create_all()

def queryDB():
        user_table = Table('user', metadata, autoload=True)
        print('user' in metadata.tables)
        print([c.name for c in user_table.columns])

        address_table = Table('address', metadata, autoload=True)
        print('address' in metadata.tables)


def insertData(user_table,  conn):
        ins = user_table.insert()
        conn.execute(ins, name='adam', fullname='Adam Gu')






