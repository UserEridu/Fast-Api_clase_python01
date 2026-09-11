from fastapi import APIRouter, HTTPException, Query
from ..db import conexion_bd
from ..schemas import ElectorBase

router = APIRouter(prefix='/electores', tags=['Electores'])

@router.get('')
def lista_electores():
    pass