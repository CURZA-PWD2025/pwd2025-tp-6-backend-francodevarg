# 🚀 Set Up del Proyecto

Este proyecto utiliza **Flask** como framework web y una capa personalizada de acceso a base de datos Relacional SQL (`ConnectDB`) sin ORM.

---

## :memo: Requisitos Previos

- Python >= 3.10
- pip
- MySQL
- Entorno virtual

---

## :wrench: Instalación

1. **Crear Entorno Virtual**

    ```bash
    python -m venv venv
    source venv/bin/activate   
    ```

2. **Instalar Dependencias**

    ```bash
    pip install -r requirements.txt
    ```
3. **Crear Archivo de Variables de Entorno**
    ```bash
    cp .env-dev .env
    ```

    Ejemplo:

    ```bash
    DB_NAME=tp_6_db
    DB_USER=root
    DB_PASSWORD=password 
    DB_HOST=localhost
    DB_PORT=3306
    FLASK_APP=app.py
    FLASK_ENV=development
    ```

4. **Correr la migracion de la DB**
    ```bash
    python db_init.py
    ```