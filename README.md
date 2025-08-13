# El Lector Curioso 📚

![Logo del Proyecto](https://raw.githubusercontent.com/Mihasustrider/lector-curioso/main/static/images/logo.png)

Un sistema de gestión para librerías o bibliotecas desarrollado con Django. La aplicación permite administrar ventas, inventario, clientes y visualizar métricas clave desde un dashboard intuitivo.

## ✨ Características Principales

-   **Dashboard Gerencial:** Visualización rápida de métricas como ventas del día, libros con stock bajo y nuevos clientes.
-   **Punto de Venta (POS):** Interfaz para registrar nuevas ventas de manera eficiente.
-   **Gestión de Inventario:** Permite agregar, editar y eliminar libros, así como controlar las existencias.
-   **Administración de Clientes:** Registro y consulta de la información de los clientes de la librería.
-   **Portal de Cliente:** Un espacio dedicado para que los clientes puedan interactuar con el sistema.

## 🛠️ Tecnologías Utilizadas

-   **Backend:** Python, Django
-   **Frontend:** HTML, CSS, JavaScript, Bootstrap 5
-   **Base de Datos:** SQLite 3 (para desarrollo)

## 🚀 Instalación y Puesta en Marcha

Sigue estos pasos para levantar un entorno de desarrollo local:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/Mihasustrider/lector-curioso.git](https://github.com/Mihasustrider/lector-curioso.git)
    cd lector-curioso
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    # Crear el entorno
    python -m venv venv

    # Activar en Windows
    .\venv\Scripts\activate

    # Activar en macOS/Linux
    source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplica las migraciones de la base de datos:**
    ```bash
    python manage.py migrate
    ```

5.  **Ejecuta el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```

6.  Abre tu navegador y ve a `http://127.0.0.1:8000/`.

## Usage

Una vez que el servidor esté corriendo, puedes acceder a las diferentes secciones a través de la barra de navegación lateral. Para acceder a la administración de Django, primero deberás crear un superusuario:

```bash
python manage.py createsuperuser