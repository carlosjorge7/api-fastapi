from peewee import *

db = MySQLDatabase(
    'blogdb',
    user='root',
    password='',
    host='localhost',
    port=3306
)

# ORM peewee crea la tabla
class User(Model):
    nombre = CharField(max_length=50)
    email = CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        database = db
        table_name = 'users'