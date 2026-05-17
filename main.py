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
