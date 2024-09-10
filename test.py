from pywithmysql.models import Table, Column
from pywithmysql.types import IntegerField, CharField
from pywithmysql.config import DataBaseConfig
from pywithmysql.settings import SettingsTable

config = DataBaseConfig(
        "localhost",
        3306,
        "29062008Kl!",
        "root",
        "test"
    )
# table = Table(
#     "users",
#     config,
#     Column("username", CharField, max_length=45, nullable=False, unique=True),
#     Column("age", IntegerField, default=18),
#     Column("email", CharField, max_length=100, unique=True, nullable=False),
#     Column("phone_number", CharField, unique=True)
# )
settings = SettingsTable(
        config,
        "users"
    )
try:
    settings.connect()
    print(settings.read_all())

except Exception as ex:
    print(f"Oh no error...\n{ex}")

finally:
    settings.disconnect()

