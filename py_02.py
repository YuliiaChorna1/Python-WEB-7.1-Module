# Робота з ORM починається зі створення об'єкта, що інкапсулює доступ до бази даних, 
# в SQLAlchemy він називається engine.

# У цьому прикладі ми використовуємо SQLite базу даних у пам'яті, 
# на диск нічого не записується:

from sqlalchemy import create_engine

engine = create_engine("sqlite:///:memory:", echo=True)
