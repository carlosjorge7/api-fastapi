import email
from typing import Optional
from typing import Optional
from pydantic import BaseModel

# Por defecto los att son requeridos, podemos ponerlos opcionales tb
class UserRequestModel(BaseModel):
    nombre: str
    email: Optional[str] = None

class UserResponseModel(UserRequestModel):
    id: int