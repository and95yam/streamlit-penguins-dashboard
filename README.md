
# 📊 Streamlit Penguins Dashboard
 
Aplicación web desarrollada con **Streamlit** para el análisis exploratorio del dataset **Palmer Penguins**, implementada siguiendo el flujo de trabajo **Gitflow** como parte de la asignatura de control de versiones.
 
---
 
## 🎯 Propósito del Proyecto
 
Este proyecto tiene como objetivo construir una herramienta interactiva de análisis de datos que permita:
 
- Cargar archivos CSV de forma dinámica desde el navegador.
- Generar visualizaciones automáticas (gráficos de barras, líneas y dispersión) para facilitar el análisis exploratorio.
- Visualizar los datos en formato tabular con filtros por posición (inicio o final del dataset).
- Validar la calidad del código mediante pruebas unitarias con pytest.
 
Todo el desarrollo fue gestionado mediante **Gitflow**, utilizando ramas `feature/*` para cada funcionalidad, una rama `develop` para integración y una rama `release/*` para la versión final publicada en `main`.
 
---
 
## 🛠️ Stack Tecnológico
 
| Tecnología | Uso |
|---|---|
| Python 3.12 | Lenguaje principal |
| Streamlit | Framework para dashboards interactivos |
| Pandas | Manipulación y análisis de datos |
| Plotly | Visualización de gráficos interactivos |
| Pytest | Pruebas unitarias |
| Git + Gitflow | Control de versiones |
 
---
 
## 📂 Estructura del Proyecto
 
```
streamlit-penguins-dashboard/
├── app.py                      # Aplicación principal Streamlit
├── src/
│   ├── __init__.py
│   └── data_utils.py           # Funciones de validación y utilidades
├── tests/
│   └── test_data_utils.py      # Pruebas unitarias con pytest
├── data/
│   └── penguins.csv            # Dataset Palmer Penguins
├── img/                        # Capturas de pantalla para el informe
├── requirements.txt            # Dependencias del proyecto
├── INFORME.md                  # Informe del desarrollo
└── README.md                   # Este archivo
```
 
---
 
## 🚀 Instalación y Ejecución
 
```bash
# Clonar el repositorio
git clone https://github.com/and95yam/streamlit-penguins-dashboard.git
cd streamlit-penguins-dashboard
 
# Crear y activar entorno virtual
python3 -m venv dash
source dash/bin/activate
 
# Instalar dependencias
pip install -r requirements.txt
 
# Ejecutar la aplicación
streamlit run app.py
 
# Ejecutar las pruebas
python -m pytest -v
```
 
---
 
## 📊 Funcionalidades
 
### 1. Carga de Archivos CSV
La aplicación permite cargar cualquier archivo CSV desde la barra lateral. Incluye validaciones de extensión, codificación y estructura del archivo.
 
### 2. Visualización de Gráficos
- **Gráfico de barras:** Suma de valores numéricos agrupados por categoría.
- **Gráfico de líneas:** Evolución de variables numéricas.
- **Gráfico de dispersión:** Relación entre dos variables numéricas.
 
### 3. Visualización Tabular
Permite visualizar los primeros o últimos N registros del dataset cargado, con control dinámico de la cantidad.
 
### 4. Pruebas Unitarias
9 pruebas unitarias que validan las funciones de carga, validación y filtrado de datos.
 
---
 
## 🔄 Flujo Gitflow Aplicado
 
```
main ← release/1.0.0 ← develop ← feature/validacion
                                 ← feature/app-principal
                                 ← feature/visualizacion-tabular
                                 ← feature/pruebas-pytest
```
 
| Rama | Propósito |
|---|---|
| `main` | Código estable en producción |
| `develop` | Integración de todas las features |
| `feature/validacion` | Funciones de validación CSV |
| `feature/app-principal` | Dashboard con gráficos interactivos |
| `feature/visualizacion-tabular` | Tabla de datos con filtros |
| `feature/pruebas-pytest` | Pruebas unitarias |
| `release/1.0.0` | Versión estable publicada |
 
---
 
## 👥 Integrantes
 
| Nombre | Rol |
|---|---|
| Andre Yamada | Desarrollo y configuración del proyecto |
| Ruperto Cisneros | Desarrollo y documentación |
 
---
 
## 📄 Licencia
 
Proyecto académico — Distrito Metropolitano de Quito, 2026.
