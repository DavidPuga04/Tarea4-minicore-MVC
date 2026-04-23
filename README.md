# Sistema de Gestión de Comisiones de Ventas (MiniCore MVC)

![Estado del Proyecto](https://img.shields.io/badge/Estado-Finalizado-blue)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Django](https://img.shields.io/badge/Django-4+-green)
![React](https://img.shields.io/badge/React-18-blue)

---

## Descripción del Proyecto
Este es un sistema web orientado a la gestión de ventas y cálculo de comisiones para vendedores. Permite registrar ventas, administrar vendedores y calcular automáticamente las comisiones según reglas definidas.

El sistema está construido bajo una arquitectura tipo **MVC**, separando claramente el backend (lógica de negocio y API) del frontend (interfaz de usuario).

---

## Funcionalidades Clave

* **Gestión de Ventas (CRUD):**
  - Crear nuevas ventas
  - Listar ventas registradas
  - Eliminar ventas

* **Gestión de Vendedores:**
  - Listado de vendedores disponibles

* **Cálculo de Comisiones:**
  - Cálculo automático basado en reglas (por monto mínimo y porcentaje)
  - Resumen de comisiones por vendedor en un rango de fechas

* **Datos de Prueba (Seed):**
  - Generación automática de vendedores y reglas de comisión

---

## Tecnologías Utilizadas

### Backend 
* **Python & Django:** Framework principal
* **Django REST Framework:** Creación de API REST
* **SQLite:** Base de datos (entorno de desarrollo)

### Frontend 
* **React.js:** Construcción de la interfaz
* **Axios:** Consumo de API REST
* **JavaScript (ES6+)**

---

## Estructura del Proyecto
```bash 
backend/
├── commissions/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│
├── config/
│ ├── settings.py
│ ├── urls.py

frontend/
├── app/
│ ├── src/
│ │ ├── services/api.js
│ │ ├── App.js
```
---

## Configuración e Instalación

### Requisitos Previos
* Python 3.10 o superior
* Node.js y npm

---

### 1. Clonar o descargar el repositorio
```bash
https://github.com/DavidPuga04/Tarea4-minicore-MVC.git
```
---
### 2. Configurar el Backend

Entra a la carpeta backend y en el terminal ejecuta:
```bash
cd backend
```
Crear y activar entorno virtual
```bash
python -m venv venv
.\venv\Scripts\activate
```
Instala dependencias
```bash
pip install -r requirements.txt
```
Si el archivo requirements.txt no contiene todas las librerías ejecuta:
```bash
pip install django djangorestframework django-cors-headers
```
Realiza las migraciones
```bash
python manage.py migrate
```
Ejecutar servidor
```bash
python manage.py runserver
```
---
### 3. Configurar el Frontend

En otra terminal ejecuta:
```bash
cd frontend/app
npm install
npm start
```
---
## Uso del Sistema
### Endpoints principales (Backend)
* GET /api/ventas/ → Listar ventas
* POST /api/ventas/ → Crear venta
* DELETE /api/ventas/{id}/ → Eliminar venta
* GET /api/vendedores/ → Listar vendedores
* GET /api/comisiones/?inicio=YYYY-MM-DD&fin=YYYY-MM-DD → Calcular comisiones por rango de fechas
* GET /api/seed/ → Generar datos de prueba

---
## Lógica de Comisiones

El sistema utiliza reglas almacenadas en la base de datos:

* Si el monto ≥ 0 → 5%
* Si el monto ≥ 500 → 10%
* Si el monto ≥ 1000 → 15%

Se aplica la regla que cumpla la condición.

---
## Conexión Frontend - Backend

El frontend consume la API mediante Axios:
```css
const api = axios.create({
  baseURL: "https://backend-mvc-5foe.onrender.com/api/"
});
```
---
## 👤 Autor
David Puga - Estudiante de Ingeniería en Software - https://github.com/DavidPuga04

--- 

## 📄 Licencia
Proyecto de uso académico para la materia de Ingeniería Web.
