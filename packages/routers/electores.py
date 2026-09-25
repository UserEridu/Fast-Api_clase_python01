from fastapi import APIRouter, HTTPException, Query
from ..db import conexion_bd
from ..schemas import ElectorBase

routers = APIRouter(prefix='/electores', tags=['Electores'])

@routers.get('')
def lista_electores():
    try:
       with conexion_bd() as conexion:
        sql: str = '''
        SELECT *
        FROM  electores
        ORDER BY id
        LIMIT 20
        '''
        cursor = conexion.execute(sql)
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    except Exception as ex:
        print(f'Fallo la conexión: {ex}')


@routers.get('/id/{id}')        
def obtener_elector(id: int):
    try:
        with conexion_bd() as conexion:
            sql:str = '''
            SELECT *
            FROM electores
            WHERE id = ? 
            '''
            cursor = conexion.execute(sql, (id,))
            row = cursor.fetchone()
            
            if not row:
                raise HTTPException(status_code=404, detail = 'Elector no encontrado')
            
            return dict(row)
    except Exception as ex:
        print(f'Fallo la conexion: {ex}')
        
@routers.get('/cedula/{cedula}')
def buscar_cedula(cedula: str):
    try:
        with conexion_bd() as conexion:
            sql:str = '''
            SELECT *
            FROM electores
            WHERE cedula = ?
            '''
            cursor = conexion.execute(sql,(cedula,))
            row = cursor.fetchone()
            
            if not row:
                 raise HTTPException(status_code=500, detail='Error interno del servidor')
             
            return dict (row)
    except Exception as ex:
        print(f'Falló la conexion: {ex}')
       