# Create (створення)

# Щоб використовувати SQLAlchemy для додавання даних до БД, нам потрібно тільки 
# створити екземпляр відповідного класу, викликати session.add і потім session.commit. 
# Всі дані в БД.

from py_08_rel_one_to_many import User, Article, session

user = User(name='Boris Johnson')
session.add(user)
session.commit()

article = Article(title='Our country’s saddest day', content='Lorem ipsum...', user_id=user.id)
session.add(article)
session.commit()

