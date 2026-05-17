from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field

app = FastAPI(
    title="API PROYECTO E.V CHARGE",
    description="Sistema de cargadores eléctricos en Bogota",
    version="1.0"
)

class Usuario(BaseModel):
    id: int = Field(gt=0, description="ID del usuario")
    nombre: str = Field(min_length=3, max_length=50, description="Nombre del usuario")
    telefono: str = Field(min_length=7, max_length=15, description="Número de teléfono")
    correo: str = Field(min_length=5, max_length=100, description="Correo electrónico")
    ciudad: str = Field(min_length=3, max_length=50, description="Ciudad del usuario")

db_usuarios = [
    {"id": 1, "nombre": "Carlos", "telefono": "3004567891", "correo": "carlos@gmail.com", "ciudad": "Bogota"},
    {"id": 2, "nombre": "Laura", "telefono": "3119876542", "correo": "laura@gmail.com", "ciudad": "Medellin"}
]
class Carga(BaseModel):
    id: int = Field(gt=0, description="ID de la carga")
    energia: float = Field(gt=0, description="Cantidad de energía")
    tiempo: int = Field(gt=0, description="Tiempo de carga")
    costo: float = Field(gt=0, description="Costo de la carga")
    estado: str = Field(min_length=3, max_length=30, description="Estado de la carga")

db_cargas = [
    {"id": 1, "energia": 45.5, "tiempo": 60, "costo": 30000, "estado": "completada"},
    {"id": 2, "energia": 30.0, "tiempo": 40, "costo": 18000, "estado": "cargando"}
]
@app.get("/usuarios")
def obtener_usuarios():
    return {
        "total": len(db_usuarios),
        "usuarios": db_usuarios,
        "status": "success"
    }


@app.get("/usuarios/{id}")
def obtener_usuario_por_id(
    id: int = Path(..., gt=0, description="ID del usuario")
):
    for usuario in db_usuarios:
        if usuario["id"] == id:
            return {
                "usuario": usuario,
                "status": "success"
            }

    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.post("/usuarios", status_code=201)
def crear_usuario(usuario: Usuario):
    db_usuarios.append(usuario.dict())

    return {
        "mensaje": "Usuario registrado exitosamente",
        "usuario": usuario,
        "status": "success"
    }


@app.get("/cargas")
def obtener_cargas():
    return {
        "total": len(db_cargas),
        "cargas": db_cargas,
        "status": "success"
    }

@app.get("/cargas/{id}")
def obtener_carga_por_id(
    id: int = Path(..., gt=0, description="ID de la carga")
):
    for carga in db_cargas:
        if carga["id"] == id:
            return {
                "carga": carga,
                "status": "success"
            }

    raise HTTPException(status_code=404, detail="Carga no encontrada")

@app.post("/cargas", status_code=201)
def crear_carga(carga: Carga):
    db_cargas.append(carga.dict())

    return {
        "mensaje": "Carga registrada exitosamente",
        "carga": carga,
        "status": "success"
    }
