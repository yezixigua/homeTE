from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import time

Base = declarative_base()


# 保存ip的对象类型， 映射一个数据表
class Visitor(Base):
    __tablename__ = 'Visitor'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    time = Column('time', String(50))
    ip = Column('ip', String(50))


# 用户&密码数据库
class User(Base):
    __tablename__ = 'User'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(50))
    password = Column('password', String(50))
    email = Column('email', String(20))
    phone = Column('phone', String(20))
    createdTime = Column('createdTime', String(50))
    lastVisitTime = Column('lastVisitTime', String(50))
    isDeleted = Column('isDeleted', String(10))

    def __init__(self, name='', pwd='', email='', phone=''):
        self.name = name
        self.password = pwd
        ct = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.email = email
        self.phone = phone
        self.createdTime = ct
        self.lastVisitTime = ct
        self.isDeleted = 'False'

    @staticmethod
    def init_data():
        Base.metadata.create_all(engine)

    def add(self):
        session1 = DB_Session()
        session1.add(self)
        session1.commit()
        session1.close()

    def __repr__(self):
        string = '' \
                 'id: {} user: {} pwd: {} ct: {} lvt: {} d: {}' \
                 ''.format(
            self.id,
            self.name,
            self.password,
            self.createdTime,
            self.lastVisitTime,
            self.isDeleted
        )
        return string

    @classmethod
    def query_data(cls, **kwargs):
        # 5. 查询数据
        # 5.1 返回结果集的第二项
        for k, v in kwargs.items():
            key, value = k, v
        print(key, value)
        # user = session.query(cls).get(key)
        user = session.query(cls).filter_by(id=1).all()
        print(user)

    @classmethod
    def query_by_name(cls, name):
        # 5. 查询数据
        # 5.1 返回结果集的第二项
        # user = session.query(cls).get(key)
        user = session.query(cls).filter_by(name=name).all()
        print(user)
        return user

    @classmethod
    def is_valid_user(cls, name, pwd):
        user = cls.query_by_name(name)[0]
        if user.password == pwd:
            return True
        else:
            return False

    @staticmethod
    def query_all():
        # 5. 查询数据
        users = session.query(User)[:]
        for user in users:
            print(user)




# 连接数据库的一些变量， 会需要全局引用
# print(os.getcwd())
DB_CONNECT_STRING = 'sqlite:///db/test2.db'
if __name__ == '__main__':
    DB_CONNECT_STRING = 'sqlite:///test2.db'
engine = create_engine(DB_CONNECT_STRING, echo=False)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()


def init_data():
    # 1. 创建表（如果表已经存在，则不会创建）
    Base.metadata.create_all(engine)


def add_data(data_ip):
    # 2. 插入数据
    session1 = DB_Session()
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    u = Visitor(time=localtime, ip=data_ip)
    session1.add(u)
    session1.commit()
    session1.close()


def add_data_user():
    # 2. 插入数据
    session1 = DB_Session()
    ct = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    u = User(name='1', password='34', createdTime=ct, lastVisitTime=ct, isDeleted='False')
    session1.add(u)
    session1.commit()
    session1.close()


def add_data_demo():
    # 2. 插入数据
    u = Visitor(time='tobi', ip='wdtf')
    u1 = Visitor(time='tobi', ip='wdtf')
    u2 = Visitor(time='tobi', ip='wdtf')
    r = Role(name='user')
    # 2.1 使用add，如果已经存在，会报错
    session.add(u)
    session.add(u1)
    session.add(u2)
    session.add(r)
    session.commit()
    print(r.id)


#
# # 3 修改数据
# # 3.1 使用merge方法，如果存在则修改，如果不存在则插入（只判断主键，不判断unique列）
# r.name = 'admin'
# session.merge(r)
#

def update_data(id_data, ip='0.0.0.0'):
    # 3.2 也可以通过这种方式修改
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    session.query(Visitor).filter(Visitor.id == id_data).update({'ip': ip, 'time': localtime})


def delete_data(id_data):
    # 4. 删除数据
    session.query(Role).filter(Role.id == id_data).delete()


def query_data(id, database=User):
    # 5. 查询数据
    # 5.1 返回结果集的第二项
    # user = session.query(database).filter_by(id=1)
    user = session.query(database).filter(database.id == id).all()
    print(user)


def query_all(database=User):
    # 5. 查询数据
    users = session.query(database)[:]
    for user in users:
        print(user)

#
# # 5.3 查询条件
# user = session.query(User).filter(User.id < 6).first()
#
# # 5.4 排序
# users = session.query(User).order_by(User.name)
#
# # 5.5 降序（需要导入desc方法）
# from sqlalchemy import desc
# users = session.query(User).order_by(desc(User.name))
#
# # 5.6 只查询部分属性
# users = session.query(User.name).order_by(desc(User.name))
# for user in users:
#     print user.name
#
# # 5.7 给结果集的列取别名
# users = session.query(User.name.label('user_name')).all()
# for user in users:
#     print user.user_name
#
# # 5.8 去重查询（需要导入distinct方法）
# from sqlalchemy import distinct
# users = session.query(distinct(User.name).label('name')).all()
#
# # 5.9 统计查询
# user_count = session.query(User.name).order_by(User.name).count()
# age_avg = session.query(func.avg(User.age)).first()
# age_sum = session.query(func.sum(User.age)).first()
#
# # 5.10 分组查询
# users = session.query(func.count(User.name).label('count'), User.age).group_by(User.age)
# for user in users:
#     print 'age:{0}, count:{1}'.format(user.age, user.count)
#
# # 6.1 exists查询(不存在则为~exists())
# from sqlalchemy.sql import exists
# session.query(User.name).filter(~exists().where(User.role_id == Role.id))
# # SELECT name AS users_name FROM users WHERE NOT EXISTS (SELECT * FROM roles WHERE users.role_id = roles.id)
#
# # 6.2 除了exists，any也可以表示EXISTS
# session.query(Role).filter(Role.users.any())
#
# # 7 random
# from sqlalchemy.sql.functions import random
# user = session.query(User).order_by(random()).first()


def my_test():
    init_data()
    a = User(name='an', pwd='a', email='1', phone='1')
    a.add()
    a.query_all()


if __name__ == '__main__':
    my_test()
    session.close()

