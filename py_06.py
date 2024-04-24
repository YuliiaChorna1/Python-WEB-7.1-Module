# Визначення відношень

# Клас Article зберігає у полі user_id зовнішній ключ на таблицю класу User. 
# Так само для query запитів ми створюємо два відношення: 
# articles у класі User та author у класі Article. 
# Параметр back_populates пов'язує ці відношення між собою. 
# Тепер ми можемо будувати двоспрямовані запити до таблиць.

from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
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
    articles = relationship('Article', back_populates='author')


class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer(), primary_key=True)
    title = Column(String(255))
    content = Column(Text())
    user_id = Column(Integer(), ForeignKey('users.id'))
    author = relationship('User', back_populates='articles')

Base.metadata.create_all(engine)
Base.metadata.bind = engine

new_user = User(name='Peter Miller')
session.add(new_user)
session.commit()

new_article = Article(title='Our countrys saddest day')
session.add(new_article)
session.commit()

users= session.query(User).filter_by(name='Peter Miller').all()

for user in users:
    for article in user.articles:
        print(article.title, user.name)

article = session.query(Article).filter_by(title='Our countrys saddest day').one()

print(article.title, article.author.name) # AttributeError: 'NoneType' object has no attribute 'name'


