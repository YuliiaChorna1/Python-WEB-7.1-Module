# Асинхронні конектори та ORM - 1

# Ви можете використовувати асинхронний режим роботи з SQLAlchemy, якщо 
# ви використовуєте діалекти, сумісні з asyncio, такі, як asyncpg, aiomysql або aiopg. 
# Для цього вам потрібно створити асинхронний движок за допомогою функції create_async_engine.
# Функція приймає URL з'єднання з додатковим параметром +asyncpg, +aiomysql або +aiopg:
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine("postgresql+asyncpg://user:password@host/database")


# Потім ви можете використовувати асинхронний движок для отримання асинхронних з'єднань
# або транзакцій за допомогою методів AsyncEngine.connect() і AsyncEngine.begin(), 
# які повертають асинхронні контекстні менеджери. 
# Ви можете виконувати SQL-запити за допомогою методів AsyncConnection.execute() або
# AsyncConnection.stream(), які повертають об'єкти Result або AsyncResult відповідно.

# async with engine.connect() as conn:
#     result = await conn.execute(select(User))
#     rows = result.fetchall()


