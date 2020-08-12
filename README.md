# Scrapy - Obtención de datos cronológicos a nivel mundial.

Proyecto Scrapy para obtencion de datos cronologicos referentes al coronavirus a nivel mundial.

Fuente: https://covidatlas.com

## Comenzando 🚀

Crea un **ambiente virtual** con el siguiente comando:
```
python3 -m venv .env
```

Activa dicho ambiente virtual e instala las **dependencias** con los siguientes comandos:
```
source .env/bin/activate
pip3 install -r requirements.txt
```

------------

***(OPCIONAL):***
Puedes cambiar `DEBUG` a `False` si deseas actualizar los registros existentes.

------------


Para **ejecutar** el proyecto simplemente realiza el siguiente comando:
```
python3 main.py
```

En la carpeta `dist` encontraras la data filtrada.

## Construido con 🛠️

* [Scrapy](https://docs.scrapy.org/en/latest/) - El framework de scraping usado

## Licencia

[Este proyecto se encutentra bajo la licencia MIT](https://opensource.org/licenses/MIT)