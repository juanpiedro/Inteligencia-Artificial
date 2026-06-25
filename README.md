# 🤖 Inteligencia Artificial y Aprendizaje Automático (IA)

Este repositorio contiene el código y los cuadernos de resolución de las prácticas de la asignatura de **Inteligencia Artificial** de la Universidad Autónoma de Madrid (UAM) correspondientes al curso 2025-26.

El proyecto abarca desde la implementación de algoritmos clásicos de búsqueda y heurísticas para juegos con adversarios, hasta la construcción, evaluación y puesta en producción de modelos predictivos de Machine Learning. Todo el entorno está desarrollado en **Python** haciendo un uso extensivo de Jupyter Notebooks.

## 🛠️ Tecnologías y Librerías

* **Lenguaje:** Python 3 (entorno Jupyter / `.ipynb`).
* **Manipulación y Análisis de Datos:** `numpy`, `pandas`.
* **Aprendizaje Automático:** `scikit-learn` (modelos de clasificación, validación cruzada, preprocesamiento y extracción de características).
* **Visualización:** `matplotlib` (representación de fronteras de decisión y distribución de datos).

## 🚀 Arquitectura y Evolución del Proyecto

El repositorio se estructura en dos grandes bloques temáticos:

### 1. Búsqueda y Juegos con Adversarios (Práctica 1)

Desarrollo de agentes inteligentes capaces de tomar decisiones eficientes en distintos entornos.

* **Búsqueda Clásica:** Implementación de algoritmos de búsqueda informada y no informada para la resolución de problemas deterministas.
* **Estrategias Competitivas:** Diseño de heurísticas para juegos de dos jugadores (ej. Reversi).
* **Torneos de IA:** Implementación algorítmica sobre árboles de juego utilizando estrategias como Minimax (y poda Alfa-Beta) para competir contra otros agentes en simulaciones.

### 2. Aprendizaje Automático / Machine Learning (Práctica 3)

Evolución desde modelos probabilísticos básicos hasta redes neuronales aplicadas sobre datos reales.

* **Modelos Probabilísticos (Parte 1):** Desarrollo de un clasificador fundamentado en el Teorema de Bayes (Gaussian Naïve Bayes).
* **Fronteras de Decisión (Parte 2):** Entrenamiento y comparación visual de distintos clasificadores (`KNeighbors`, `Decision Tree`, `Logistic Regression`, `MLP Neural Network`) aplicados sobre bases de datos sintéticas no lineales (moons, circles, blobs).
* **Bases de Datos Reales (Parte 3):** Preprocesamiento, extracción de estadísticos y evaluación de modelos utilizando validación cruzada (`cross_val_score`) sobre bases de datos complejas (ej. *German Credit Data*).
* **Puesta en Producción (Parte 4):** Diseño de un modelo final orientado a la explotación comercial para una startup, resolviendo problemas de predicción como las calificaciones ESRB de videojuegos, la adopción de mascotas o la experiencia de usuarios en gimnasios.

## ⚙️ Instalación y Uso

Para ejecutar los algoritmos y visualizar los cuadernos de aprendizaje automático, es necesario disponer de un entorno compatible con Jupyter y las dependencias correspondientes instaladas.

1. **Instalación de dependencias:**
```bash
pip install numpy pandas matplotlib scikit-learn jupyter

```


2. **Ejecución de los cuadernos:**
```bash
jupyter notebook

```


*Navega hasta los ficheros `p3_01.ipynb` a `p3_04.ipynb` y asegúrate de ejecutar las celdas secuencialmente para generar los modelos y gráficos de validación.*

## 👨‍💻 Autor

* **Juan Herrero Pérez** - Estudiante de Ingeniería Informática (Universidad Autónoma de Madrid)
