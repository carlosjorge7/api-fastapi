from fastapi import FastAPI, HTTPException

from database import db as connection
from database import User

from schemas import UserRequestModel, UserResponseModel

app = FastAPI(title='api restful',
            description='Prueba del framework', 
            version='1.0.0')

# Antes de que el servidor arranque
@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([User])

# Despues de que el servidor arranque
@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()


@app.get('/')
async def index():
    return 'Hola mundo'

@app.post('/users')
async def create_user(user: UserRequestModel):
    User.create(
        nombre = user.nombre,
        email = user.email
    )
    return user

@app.get('/users/{id}')
async def get_user(id):
    user = User.select().where(User.id == id).first()

    if user:
        return UserResponseModel(id = user.id,
                                nombre = user.nombre,
                                email = user.email)
    else:
        return HTTPException(404, 'User not found')

@app.delete('/users/{id}')
async def delete_user(id):
    user = User.select().where(User.id == id).first()

    if user:
        user.delete_instance()
        return True
    else:
        return HTTPException(404, 'User not found')
