from pydantic import BaseModel, Field

type Opcional = str| None
class ElectorBase(BaseModel):
    nacionalidad:Opcional = None
    cedula:str = Field(min_length=1)
    apellidos_nombres:Opcional = None
    centro:str = Field(min_length=1)
    fecha_nacimiento:Opcional = None