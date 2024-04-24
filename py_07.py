# Визначення відношень

# Якщо з якоїсь причини нам потрібно визначити відношення один до одного, 
# то воно будується на відношенні один до багатьох за допомогою параметра uselist

# Параметр backref є аналогом раніше розглянутого параметра back_populates. 
# Відмінність у тому, що відношення з параметром backref достатньо оголосити в одному класі,
# щоб можна було б будувати двоспрямовані запити з query.

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///sqlalchemy_example_2.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    name = Column(String(20))
    userinfo = relationship('UserInfo', backref='user', uselist=False)


class UserInfo(Base):
    __tablename__ = 'userinfo'
    id = Column(Integer(), primary_key=True)
    telegram = Column(String(11))
    phone = Column(String(11))
    site = Column(String(64))
    user_id = Column(Integer(), ForeignKey('users.id'))
