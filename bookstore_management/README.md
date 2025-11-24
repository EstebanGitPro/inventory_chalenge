# Sistema de Gestión de Librería

Este es un sistema de consola robusto para gestionar el inventario y las ventas de una librería. El proyecto está diseñado con una arquitectura modular y cumple con requisitos estrictos de validación y reporte.

## Características Principales

### 1. Gestión de Inventario
- **Registrar Productos**: Permite agregar nuevos libros con título, autor, categoría, precio y stock.
- **Actualizar**: Modificar el precio o la cantidad de stock de libros existentes.
- **Eliminar**: Dar de baja productos del inventario.
- **Consultar**: Ver una tabla detallada con todos los productos disponibles.

### 2. Sistema de Ventas
- **Registro de Ventas**: Procesa ventas validando automáticamente la disponibilidad de stock.
- **Descuentos Automáticos**: Aplica un 10% de descuento si la cantidad comprada es mayor a 5 unidades.
- **Historial**: Mantiene un registro completo de todas las transacciones realizadas.

### 3. Reportes Avanzados
- **Top Ventas**: Muestra los 3 productos más vendidos.
- **Ventas por Autor**: Agrupa y suma los ingresos generados por cada autor.
- **Reporte Financiero**: Calcula ingresos brutos, descuentos otorgados e ingresos netos.

## Estructura del Proyecto

El código está organizado de manera modular en la carpeta `src`:

```text
bookstore_management/
├── src/
│   ├── data/
│   │   ├── adapter.py       # Manejo de lectura/escritura de datos (JSON)
│   │   └── store_data.json  # Base de datos de productos y ventas
│   ├── main.py              # Punto de entrada y menús del sistema
│   ├── products.py          # Lógica de gestión de productos
│   ├── sales.py             # Lógica de registro de ventas
│   ├── reports.py           # Generación de estadísticas
│   └── utils.py             # Funciones de validación y formato (sin emojis)
└── test_system.py           # Script de pruebas automatizadas
```

## Requisitos e Instalación

1. **Requisitos**: Python 3.x instalado.
2. **Instalación**: No requiere librerías externas.

## Cómo Ejecutar

Para iniciar el sistema, navega a la carpeta del proyecto y ejecuta el archivo principal:

```bash
cd inventory_chalenge/bookstore_management
python3 src/main.py
```

## Datos de Prueba

El sistema viene precargado con 5 libros clásicos (como "The Great Gatsby", "1984") para facilitar las pruebas inmediatas.

## Notas de Desarrollo

- **Idioma**: La interfaz de usuario y el código están en inglés (según requerimiento).
- **Interfaz**: Diseño limpio y profesional sin uso de emojis.
- **Persistencia**: Los datos se guardan automáticamente en `src/data/store_data.json`.
