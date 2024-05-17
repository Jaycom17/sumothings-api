# API para la app de sumothings
## Configuración de directorios
  ``` Text
  sumothings-api
  ├─ 📁src
  │  ├─ 📁config
  │  │  └─ 📄config.py
  │  ├─ 📁controllers
  │  │  └─ 📄ProductsController.py
  │  ├─ 📁database
  │  │  └─ 📄Database.py
  │  ├─ 📁middlewares
  │  │  └─ 📄AuthMiddleware.py
  │  ├─ 📁models
  │  │  └─ 📄ProductModel.py
  │  ├─ 📁routes
  │  │  └─ 📄ProductsRoutes.py
  │  ├─ 📁services
  │  │  └─ 📄ProductsServices.py
  │  ├─ 📁utils
  │  │  └─ 📄Any.py
  │  └─ 📄index.py
  ├─ 📄.env
  ├─ 📄Dockerfile
  ├─ 📄README.md
  └─ 📄requirements.txt
  ```
### Descripción
**Directorios:** En cada carpeta hay un ejemplo de como se nombrarian los archivos a crear  

**Programación:** Programación funcional  

**Nomencaltura:** cammelCase, ejemplo: crearProducto()  

### A tomar en cuenta
En el archivo *.env* se tienen variables de entorno, las cuales sireven para ser configuradas en el equipo personal de cada uno, el archivo subido ahi se puede tomar como ejemplo de lo que cada persona deberia tener en su equipo, dentro del *.gitignore* debe estar ese archivo para que cada uno trabaje con eso configurado en su equipo, en el archivo config/config.py se tiene un ejemplo tambien de como leer esas variables de entorno.  

Para hacer la instalación de los requerimientos se hace uso del comando:
```bash
  pip install -r requirements.txt
```
Y para generarlo:
```bash
pip freeze > requirements.txt
```

Trabajar en un entorno virtual (virtualenv)
