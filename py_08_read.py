# Read (читання)

# Якщо ми знаємо ідентифікатор користувача, ми можемо використовувати метод get. 
# Метод для отримання значення поля може безпосередньо використовувати властивості класу:

from py_08_rel_one_to_many import User, Article, session

user = session.query(User).get(1)
print(user.id, user.name)

# Метод all використовують, щоб отримати всі результати запиту:

users = session.query(User).all()

for user in users:
    print(user.id, user.name)

# Є також методи first, scalar з one. Різниця між трьома:
# .first — Повертає перший об'єкт запису, якщо він є.
# .one — Запитує всі рядки і викликає виняток, якщо щось повертається, крім одного результату.
# .scalar — Повертає перший елемент першого результату, None, якщо результату немає,
# або помилку, якщо їх більше ніж один результат.

# Метод filter_by використовується для фільтрації за певним полем, 
# або його аналог метод filter трохи з іншим синтаксисом. Давайте відфільтруємо за полем:

user1 = session.query(User).filter_by(name='Boris Johnson').first()
user2 = session.query(User).filter(User.name == 'Boris Johnson').scalar()
print(user1.id, user1.name)
print(user2.id, user2.name)


