from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey, select
import time
# import pymysql
# pymysql.install_as_MySQLdb()



# SQLite 连接engin方式
engine = create_engine('sqlite:///test1.db', echo=True)
metadata = MetaData(engine)

conn = engine.connect()

# MYSQL连接engin方式
# engine = create_engine('mysql+mysqldb://root:zz168601ZZ@localhost/test', echo=True)
# metadata = MetaData(engine)


def init_data():
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


def query_data():
        user_table = Table('user', metadata, autoload=True)
        print('user' in metadata.tables)
        print([c.time for c in user_table.columns])

        address_table = Table('address', metadata, autoload=True)
        print('address' in metadata.tables)


def insert_data(conn, ip):
        user_table = Table('user', metadata, autoload=True)
        ins = user_table.insert()
        localtime = time.asctime(time.localtime(time.time()))
        conn.execute(ins, time=localtime, ip=ip)


if __name__ == '__main__':
    init_data()
    query_data()
    # insert_data(conn, '129.9.0.1')
    # insert_data(conn, '165.9.0.1')
    # insert_data(conn, '123.9.0.1')
    # query_data()

