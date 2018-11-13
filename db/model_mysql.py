# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql


pymysql.install_as_MySQLdb()

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    ip = Column(String(20))

# 初始化数据库连接:
# engine = create_engine('mysql://root:zz168601ZZ@localhost:3306/test')
engine = create_engine('sqlite:///test.db')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)




def testdb_save():
    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    new_user = User(id='5', ip='127.0.0.1')
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

def testdb_query():
    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(User).all()
    # 打印类型和对象的name属性:
    print(user)
    # 关闭Session:
    session.close()

if __name__ == '__main__':
    testdb_query()

