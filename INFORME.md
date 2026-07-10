# 📋 Informe de Desarrollo — Streamlit Penguins Dashboard

---

### 👥 Integrantes

| Nombre | Carrera |
|---|---|
| **Andre Yamada** | Ingeniería en Software |
| **Ruperto Cisneros** | Ingeniería en Software |

---

## 1. Objetivo

Desarrollar una aplicación interactiva en Streamlit para el análisis exploratorio del dataset Palmer Penguins, aplicando Gitflow como flujo de control de versiones.

---

## 2. Flujo Gitflow Aplicado

```
main ─────────────────────────────────────── ● v1.0.0
                                            ↑
release/1.0.0 ─────────────────────────── ●
                                            ↑
develop ── ● ── ● ── ● ── ● ── ● ─────── ●
            ↑    ↑    ↑    ↑
            │    │    │    └── feature/pruebas-pytest
            │    │    └─────── feature/visualizacion-tabular
            │    └──────────── feature/app-principal
            └───────────────── feature/validacion
```

---

## 3. Desarrollo por Features

### 3.1 Feature: Funciones de Validación

📂 Rama: `feature/validacion`

Se implementaron las funciones de validación y carga de archivos CSV en `src/data_utils.py`, incluyendo validación de extensión, manejo de codificaciones y funciones para obtener columnas numéricas, categóricas y filtrar registros.

---

### 3.2 Feature: Aplicación Principal — Dashboard

📂 Rama: `feature/app-principal`

Se desarrolló la aplicación principal en `app.py` con carga de archivos CSV y tres tipos de gráficos interactivos.

#### 📸 Dashboard — Gráfico de barras y gráfico de líneas

![Dashboard gráficos](img/dashboard-graficos.png)

#### 📸 Dashboard — Gráfico de dispersión

![Gráfico de dispersión](img/grafico-dispersion.png)

---

### 3.3 Feature: Visualización Tabular

📂 Rama: `feature/visualizacion-tabular`

Se agregó la funcionalidad de visualización tabular que permite seleccionar la cantidad de registros y la posición de lectura (inicio o final del dataset).

#### 📸 Visualización tabular de datos

![Visualización tabular](img/visualizacion-tabular.png)

---

### 3.4 Feature: Pruebas con Pytest

📂 Rama: `feature/pruebas-pytest`

Se implementaron 9 pruebas unitarias que validan las funciones de carga, validación y filtrado de datos.

| # | Prueba | Resultado |
|---|---|---|
| 1 | Validar extensión CSV correcta | ✅ PASSED |
| 2 | Validar extensión CSV mayúscula | ✅ PASSED |
| 3 | Validar extensión incorrecta | ✅ PASSED |
| 4 | Obtener columnas numéricas | ✅ PASSED |
| 5 | Obtener columnas categóricas | ✅ PASSED |
| 6 | Filtrar registros desde el inicio | ✅ PASSED |
| 7 | Filtrar registros desde el final | ✅ PASSED |
| 8 | Error con cantidad inválida | ✅ PASSED |
| 9 | Error con posición inválida | ✅ PASSED |

#### 📸 Ejecución de pytest

![Resultados pytest](img/pytest-resultados.png)

---

### 3.5 Release 1.0.0

Se creó la rama `release/1.0.0` desde `develop`, se realizó el merge hacia `main` con `--no-ff` y se etiquetó con `v1.0.0`.

#### 📸 Historial Gitflow

![Git log](img/gitflow-log.png)

---

## 4. Conclusiones

**Conclusión 1 — Aislamiento de funcionalidades mediante ramas feature:** Gitflow permite desarrollar cada funcionalidad de forma aislada en su propia rama `feature/*`, lo que evita que un error en una funcionalidad en desarrollo afecte al código estable de `develop` o `main`. En este proyecto, las funciones de validación, la aplicación principal, la visualización tabular y las pruebas se desarrollaron de forma independiente, y cada una fue integrada a `develop` solo cuando estaba completa y funcional. Este aislamiento reduce significativamente el riesgo de introducir regresiones en el código base.

**Conclusión 2 — Trazabilidad del historial de cambios:** El uso de ramas nombradas con convención (`feature/`, `release/`) junto con mensajes de commit descriptivos (`feat:`, `test:`, `release:`) y merges explícitos con `--no-ff` genera un historial de Git no lineal que permite reconstruir exactamente qué se hizo, cuándo y por qué. Esto es especialmente valioso en equipos de trabajo donde múltiples desarrolladores contribuyen al mismo proyecto.

**Conclusión 3 — Separación entre desarrollo y producción:** La rama `develop` actúa como zona de integración donde se prueban todas las funcionalidades juntas antes de promoverlas a `main` mediante un `release`. Esto garantiza que la rama `main` siempre contiene código estable y listo para producción. La rama `release` agrega una capa adicional de control al congelar el código para revisión final antes de la publicación.

---

## 5. Repositorios

| Integrante | URL |
|---|---|
| Andre Yamada | https://github.com/and95yam/streamlit-penguins-dashboard |
| Ruperto Cisneros | https://github.com/srcisneros/streamlit-penguins-dashboard-Public |

---

