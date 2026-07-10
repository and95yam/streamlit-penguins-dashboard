# 📊 Streamlit Penguins Dashboard

Aplicación web interactiva desarrollada con **Streamlit** para el análisis exploratorio del dataset **Palmer Penguins**, implementada aplicando el flujo de trabajo **Gitflow**.

---

## 🎯 Propósito

Herramienta de análisis de datos que permite cargar archivos CSV, generar visualizaciones automáticas y explorar los datos de forma tabular, orientada al estudio de las características físicas de tres especies de pingüinos antárticos.

---

## 📂 Estructura del Proyecto

```
streamlit-penguins-dashboard/
├── app.py                      # Aplicación principal Streamlit
├── src/
│   ├── __init__.py
│   └── data_utils.py           # Funciones de validación y utilidades
├── tests/
│   └── test_data_utils.py      # Pruebas unitarias (9 tests)
├── data/
│   └── penguins.csv            # Dataset Palmer Penguins
├── img/                        # Capturas de pantalla
├── requirements.txt            # Dependencias
├── INFORME.md                  # Informe de desarrollo
└── README.md
```

---

## 🛠️ Stack Tecnológico

| Tecnología | Uso |
|---|---|
| Python 3.12 | Lenguaje principal |
| Streamlit | Dashboards interactivos |
| Pandas | Manipulación de datos |
| Plotly | Gráficos interactivos |
| Pytest | Pruebas unitarias |
| Git + Gitflow | Control de versiones |

---

## 📊 Funcionalidades

| Funcionalidad | Descripción |
|---|---|
| Carga de CSV | Validación de extensión, codificación y estructura |
| Gráfico de barras | Suma de valores numéricos por categoría |
| Gráfico de líneas | Evolución de variables numéricas |
| Gráfico de dispersión | Relación entre dos variables |
| Vista tabular | Primeros o últimos N registros del dataset |
| Pruebas unitarias | 9 tests que validan las funciones del sistema |

---

## 🔄 Flujo Gitflow

```
main ← release/1.0.0 ← develop ← feature/validacion
                                 ← feature/app-principal
                                 ← feature/visualizacion-tabular
                                 ← feature/pruebas-pytest
```

| Rama | Propósito |
|---|---|
| `main` | Código estable en producción |
| `develop` | Integración de features |
| `feature/validacion` | Funciones de validación CSV |
| `feature/app-principal` | Dashboard con gráficos |
| `feature/visualizacion-tabular` | Tabla de datos con filtros |
| `feature/pruebas-pytest` | Pruebas unitarias |
| `release/1.0.0` | Versión estable publicada |

---

## 👥 Integrantes

| Nombre | Rol |
|---|---|
| Andre Yamada | Desarrollo y configuración |
| Ruperto Cisneros | Desarrollo y documentación |

---


