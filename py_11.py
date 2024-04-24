# SQLAlchemy 2.0

# Визначення моделей​
# Визначимо наші класи-моделі, які успадковуються від класу Base і 
# відповідають таблицям у базі даних.

from sqlalchemy import create_engine, Integer, String, ForeignKey, select, Text, and_, or_, not_, desc, func
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship

engine = create_engine('sqlite:///:memory:', echo=False)  
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String)


class Post(Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[str] = mapped_column('user_id', Integer, ForeignKey('users.id'))
    user: Mapped['User'] = relationship(User)


Base.metadata.create_all(engine)



if __name__ == '__main__':

    # Додамо нових користувачів зі списку names у базу даних:
    names = ['Crystal Najera', 'Shaun Beck', 'Kathrin Reinhardt']
    for name in names:
        user = User(fullname=name)
        session.add(user)
    session.commit()

    # Запити до бази даних, ex.: вибрати всі записи з таблиці users:
    stmt = select(User)
    result = session.execute(stmt)
    for user in result.scalars():
        print(user.id, user.fullname)

    # для вибірки певних стовпчиків із таблиці:
    stmt = select(User.id, User.fullname)
    result = session.execute(stmt)
    users = []
    for row in result:
        print(row)
        users.append(row)

    # Фільтрація записів: за виразами порівняння, логічними операторами або ін:
    stmt = select(User).where(User.fullname == "Shaun Beck")
    result = session.execute(stmt).scalar_one()
    print(result.id, result.fullname)

    # Фільтрація записів: різні оператори для порівняння колонок 
    # зі значеннями або іншими колонками, такі як як ==, !=, <, >, <=, >=, in_, like, ilike
    stmt = select(User).where(User.fullname.like("%ha%"))
    result = session.execute(stmt)
    for user in result.scalars().all():
        print(user.id, user.fullname)

    # Фільтрація записів: логічні оператори для комбінування кількох критеріїв 
    # в одну умову where, такі як and_, or_, not_ :
    stmt = select(User).where(and_(User.fullname.like("%ha%"), User.fullname != 'Shaun Beck'))
    result = session.execute(stmt)
    for user in result.scalars():
        print(user.id, user.fullname)

    # Фільтрація записів: метод where() кілька разів. Це аналог додавання 
    # декількох критеріїв в одну умову where, за допомогою оператора and_ :
    stmt = select(User).where(User.fullname.like("%ha%")).where(User.fullname != 'Shaun Beck')
    result = session.execute(stmt)
    for user in result.scalars().all():
        print(user.id, user.fullname)

    # Сортування записів: за певним критерієм - метод order_by() об'єкта Select:
    stmt = select(User).order_by(User.fullname)
    result = session.execute(stmt)
    for user in result.scalars():
        print(user.id, user.fullname)

    # Сортування записів: метод desc() або asc() для сортування за зменшенням або зростанням:
    stmt = select(User).order_by(desc(User.fullname))
    result = session.execute(stmt)
    for user in result.scalars():
        print(user.id, user.fullname)

    ########### Запити з JOIN:
    stmt = select(User.id, User.fullname)
    result = session.execute(stmt)
    users = []
    for row in result:
        users.append(row)

    for user in users: # створюємо запис Post для кожного користувача
        post = Post(title=f'Title {user[1]}', body=f'Body post user {user[1]}', user_id=user[0])
        session.add(post)
    session.commit()
    
    stmt = (
        select(User.fullname, func.count(Post.id))  # створюємо об'єкт select із вибіркою імені користувача та кількості постів
        .join(Post)  # робимо join з моделлю Post за зовнішнім ключем user_id
        .group_by(User.fullname)  # групуємо результати за ім'ям користувача
    )
    results = session.execute(stmt).all()  # виконуємо запит і отримуємо список кортежів
    for name, count in results:  # перебираємо результати
        print(f"{name} has {count} posts")  # виводимо ім'я користувача та кількість постів

