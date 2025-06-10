# 📚 Documentación de API

## Descripción
API RESTful desarrollada con Flask.
---

## MARCAS Endpoints

---

## GET /marcas/

- **URL:** `/marcas/`
- **Método:** `GET`
- **Descripción:** Retorna todas las marcas registradas.

### Respuestas:
- **200 OK**

```json
[
    {
        "id": 1,
        "nombre": "Marca A"
    },
    {
        "id": 2,
        "nombre": "Marca B"
    }
]
```

- **400 OK**
```json
{
    "mensaje": "No hay marcas registradas"
}
```


- **500 OK**

```json
{
    "mensaje": " error : <detalle>"
}
```



---

## GET /marcas/{id}

- **URL:** `/marcas/<int:id>`
- **Método:** `GET`
- **Descripción:** Retorna una marca específica por su ID.

### Respuestas:
- **200 OK**
```json
{
    "id": 1,
    "nombre": "Marca A"
}
```

- **404 OK**
```json
{
    "mensaje": " error : Marca no encontrada"
}
```

- **500 OK**
```json
{
    "mensaje": " error : <detalle>"
}
```

---

## POST /marcas/

- **URL:** `/marcas/`
- **Método:** `POST`
- **Descripción:** Crea una nueva marca.

### Cuerpo del Request:
```json
{
    "nombre": "Nueva Marca"
}
```

### Respuestas:
- **201 Created**
```json
{
    "mensaje": "Marca creada con éxito"
}
```

- **400 Bad Request**
```json
{
    "mensaje": "La descripción es requerida"
}
```

- **500 OK**
```json
{
    "mensaje": "Error: <detalle>"
}
```

---

## PUT /marcas/{id}

- **URL:** `/marcas/<int:id>`
- **Método:** `PUT`
- **Descripción:** Actualiza una marca existente.

### Cuerpo del Request:
```json
{
    "id": 1,
    "nombre": "Marca Actualizada"
}
```

### Respuestas:
- **200 OK**
```json
{
    "mensaje": "Marca actualizada con éxito"
}
```

- **400 Bad Request**
```json
{
    "mensaje": "La descripción es requerida"
}
```

- **404 Not Found**
```json
{
    "message": "La marca con ID 1 que intenta actualizar no existe"
}
```

- **500 OK**
```json
{
    "mensaje": "Error: <detalle>"
}
```

---

## DELETE /marcas/<id>

- **URL:** `/marcas/<int:id>`
- **Método:** `DELETE`
- **Descripción:** Elimina una marca existente.

### Respuestas:
- **200 OK**
```json
{
    "mensaje": "Marca eliminada con éxito"
}
```

- **400 Bad Request**
```json
{
    "mensaje": "No se pudo eliminar la marca"
}
```

- **500 OK**
```json
{
    "mensaje": "Error: <detalle>"
}
```

---

## Autenticación

> Actualmente esta API **NO requiere autenticación** (pública).

---

## Notas

- Todos los endpoints retornan respuestas en formato **JSON**.
- Manejo básico de errores implementado.
- En producción se recomienda añadir validaciones más estrictas y autenticación (por ejemplo, JWT).

---