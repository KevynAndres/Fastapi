from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(
    title="API PROYECTO E.V CHARGE",
    description="Sistema de cargadores eléctricos en Bogota",
    version="1.0"
)

contador_id = 3

@app.get("/carros")
def obtener_carros(
    estado: Optional[str] = Query(None, description="Filtrar por estado"),
    tipo: Optional[str] = Query(None, description="Filtrar por tipo de cargador")
):
    return {
        "status": "success"
    }

@app.get("/carros/{id}")
def obtener_carro_por_id(
    id: int = Path(..., gt=0, description="ID del carro")
):
    return {
        "status": "success"
    }

@app.get("/carros/placa/{placa}")
def obtener_carro_por_placa(
    placa: str = Path(..., min_length=5, max_length=10, description="Placa del carro")
):
    return {
        "status": "success"
    }

@app.post("/carros", status_code=201)
def crear_carro():
    return {
        "status": "success"
    }