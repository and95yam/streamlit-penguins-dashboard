# 🐧📊 Streamlit Penguins Dashboard

<p align="center">
  <img src="img/dashboard-principal.png" alt="Dashboard Streamlit Penguins" width="750">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-purple?style=for-the-badge&logo=pandas">
  <img src="https://img.shields.io/badge/Plotly-Interactive%20Charts-orange?style=for-the-badge&logo=plotly">
  <img src="https://img.shields.io/badge/Pytest-Unit%20Testing-green?style=for-the-badge&logo=pytest">
</p>

---

## 🌟 Descripción General

**Streamlit Penguins Dashboard** es una aplicación web interactiva desarrollada con **Streamlit** para realizar análisis exploratorio de datos sobre el dataset **Palmer Penguins**.

El sistema permite cargar archivos CSV, visualizar datos de forma dinámica, generar gráficos interactivos y validar el funcionamiento del código mediante pruebas unitarias con **pytest**.

Este proyecto fue desarrollado como parte de la asignatura de **Control de Versiones**, aplicando el flujo de trabajo **Gitflow** con ramas `feature/*`, `develop`, `release/*` y `main`.

---

## 🎯 Propósito del Proyecto

El objetivo principal del proyecto es construir una herramienta visual, sencilla e interactiva que facilite el análisis de datos mediante un dashboard web.

La aplicación permite:

* 📂 Cargar archivos CSV desde el navegador.
* 📊 Generar gráficos automáticos e interactivos.
* 🔎 Explorar datos en formato tabular.
* 🧪 Ejecutar pruebas unitarias con pytest.
* 🌱 Aplicar correctamente el flujo de trabajo Gitflow.
* 🚀 Publicar una versión estable del proyecto en la rama `main`.

---

## 🖼️ Vista General del Dashboard

<p align="center">
  <img src="img/vista-dashboard.png" alt="Vista general del dashboard" width="700">
</p>

El dashboard cuenta con una interfaz amigable donde el usuario puede cargar datos, seleccionar variables y visualizar información de forma clara.

---

## 🛠️ Stack Tecnológico

| Tecnología           | Uso Principal                             |
| -------------------- | ----------------------------------------- |
| 🐍 **Python 3.12**   | Lenguaje principal del proyecto           |
| 📊 **Streamlit**     | Creación del dashboard interactivo        |
| 🧮 **Pandas**        | Manipulación, lectura y análisis de datos |
| 📈 **Plotly**        | Generación de gráficos interactivos       |
| 🧪 **Pytest**        | Validación mediante pruebas unitarias     |
| 🌿 **Git + Gitflow** | Control de versiones y gestión de ramas   |

---

## 📂 Estructura del Proyecto

```bash
streamlit-penguins-dashboard/
├── app.py                      # Aplicación principal Streamlit
├── src/
│   ├── __init__.py
│   └── data_utils.py           # Funciones de validación y utilidades
├── tests/
│   └── test_data_utils.py      # Pruebas unitarias con pytest
├── data/
│   └── penguins.csv            # Dataset Palmer Penguins
├── img/                        # Capturas e imágenes del proyecto
├── requirements.txt            # Dependencias del proyecto
├── INFORME.md                  # Informe técnico del desarrollo
└── README.md                   # Documentación principal
```

---

## 🚀 Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/and95yam/streamlit-penguins-dashboard.git
cd streamlit-penguins-dashboard
```

### 2. Crear entorno virtual

```bash
python3 -m venv dash
```

### 3. Activar entorno virtual

En Linux o Mac:

```bash
source dash/bin/activate
```

En Windows con Git Bash:

```bash
source dash/Scripts/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar la aplicación

```bash
streamlit run app.py
```

### 6. Ejecutar pruebas unitarias

```bash
python -m pytest -v
```

---

## 📊 Funcionalidades Principales

### 1. 📂 Carga de Archivos CSV

La aplicación permite cargar archivos CSV directamente desde la barra lateral del dashboard.

Incluye validaciones para:

* Extensión del archivo.
* Lectura correcta del CSV.
* Estructura del dataset.
* Existencia de columnas numéricas y categóricas.

<p align="center">
  <img src="img/carga-csv.png" alt="Carga de archivos CSV" width="650">
</p>

---

### 2. 📈 Visualización de Gráficos

El sistema genera gráficos interactivos que facilitan el análisis exploratorio de datos.

Tipos de gráficos implementados:

| Gráfico           | Descripción                                                 |
| ----------------- | ----------------------------------------------------------- |
| 📊 **Barras**     | Permite sumar valores numéricos agrupados por una categoría |
| 📉 **Líneas**     | Permite visualizar la evolución de variables numéricas      |
| 🔵 **Dispersión** | Permite analizar la relación entre dos variables numéricas  |

<p align="center">
  <img src="img/graficos.png" alt="Gráficos interactivos" width="700">
</p>

---

### 3. 📋 Visualización Tabular

La aplicación permite visualizar los datos en forma de tabla, seleccionando dinámicamente la cantidad de registros.

Opciones disponibles:

* Ver primeros registros del dataset.
* Ver últimos registros del dataset.
* Seleccionar la cantidad de filas a mostrar.
* Explorar los datos de forma ordenada.

<p align="center">
  <img src="img/tabla-datos.png" alt="Visualización tabular" width="700">
</p>

---

### 4. 🧪 Pruebas Unitarias

El proyecto incluye pruebas unitarias desarrolladas con **pytest** para validar el correcto funcionamiento de las funciones principales.

Se implementaron **9 pruebas unitarias** enfocadas en:

* Carga de archivos CSV.
* Validación de columnas.
* Validación de datos vacíos.
* Filtrado de registros.
* Manejo de errores.

<p align="center">
  <img src="img/pytest-resultados.png" alt="Resultados pytest" width="700">
</p>

---

## 🔄 Flujo Gitflow Aplicado

El desarrollo del proyecto se gestionó mediante **Gitflow**, utilizando ramas separadas para cada funcionalidad.

```bash
main
 └── release/1.0.0
      └── develop
           ├── feature/validacion
           ├── feature/app-principal
           ├── feature/visualizacion-tabular
           └── feature/pruebas-pytest
```

<p align="center">
  <img src="img/gitflow.png" alt="Flujo Gitflow aplicado" width="700">
</p>

---

## 🌿 Ramas del Proyecto

| Rama                            | Propósito                                            |
| ------------------------------- | ---------------------------------------------------- |
| `main`                          | Contiene la versión estable y final del proyecto     |
| `develop`                       | Integra todas las funcionalidades desarrolladas      |
| `feature/validacion`            | Contiene las funciones de validación del archivo CSV |
| `feature/app-principal`         | Contiene la construcción principal del dashboard     |
| `feature/visualizacion-tabular` | Contiene la funcionalidad de visualización de datos  |
| `feature/pruebas-pytest`        | Contiene las pruebas unitarias del proyecto          |
| `release/1.0.0`                 | Rama utilizada para preparar la versión final        |

---

## 🧪 Resultado de Pruebas

```bash
python -m pytest -v
```

Resultado esperado:

```bash
9 passed
```

Esto confirma que las funciones principales del proyecto fueron validadas correctamente antes de publicar la versión final.

---

## 👥 Integrantes

| Nombre               | Rol                                     |
| -------------------- | --------------------------------------- |
| **Andre Yamada**     | Desarrollo y configuración del proyecto |
| **Ruperto Cisneros** | Desarrollo y documentación              |

---

## 📌 Conclusión

El proyecto **Streamlit Penguins Dashboard** permitió aplicar conocimientos de análisis de datos, desarrollo web con Python, visualización interactiva y control de versiones mediante Gitflow.

Además, se logró estructurar un flujo de trabajo ordenado, validado con pruebas unitarias y documentado adecuadamente para facilitar su instalación, ejecución y mantenimiento.

---

## 📄 Licencia

Proyecto académico — Distrito Metropolitano de Quito, 2026.

<p align="center">
  <b>🐧 Desarrollado con Python, Streamlit y Gitflow 🐧</b>
</p>
