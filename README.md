# **Guía de uso**

> [!IMPORTANT]
> En caso de no desear instalar las librerías, el archivo  `main.ipynb` contiene toda la ejecuciones ya 
> realizadas, de forma que no se requiere volver a ejecutarlas.


## Instalación
Se recomienda hacer uso de ***Python 3.9.13***, ya que versiones posteriores han presentado problemas de compatibilidad con las librerías. La forma más cómoda de cambiar de versión de Python es con [pyenv](https://pyenv-win.github.io/pyenv-win/).

Para clonar el repositorio en el ordenador, se debe ejecutar el siguiente comando:

```bash
git clone https://github.com/Pablomg02/DRL-Opt
```

Si se desea realizar en un entorno virtual y así evitar modificar las librerías actuales, se deben ejecutar los siguientes comandos:

```bash
python -m venv venv
venv\Scripts\activate
```

Para instalar las dependencias, solo hace falta correr el siguiente comando en el directorio del repositorio:

```bash
pip install -r requirements.txt
```

## Código
El trabajo puede ser ejecutado paso a paso haciendo uso del archivo `main.ipynb`, un archivo tipo Notebook que permite realizar las diferentes partes paso a paso. Ahí, se pueden observar diferentes anotaciones.