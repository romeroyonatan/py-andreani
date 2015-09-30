[![Coverage Status](https://coveralls.io/repos/romeroyonatan/py-andreani/badge.svg?branch=master&service=github)](https://coveralls.io/github/romeroyonatan/py-andreani?branch=master)
[![Build Status](https://travis-ci.org/romeroyonatan/py-andreani.svg?branch=master)](https://travis-ci.org/romeroyonatan/py-andreani)
[![Python version](https://img.shields.io/badge/python-3.2%203.3%203.4%203.5-blue.svg)](https://travis-ci.org/romeroyonatan/py-andreani)
[![License](https://img.shields.io/badge/license-GPLv2-yellow.svg?style=flat-square)](https://github.com/romeroyonatan/py-andreani/blob/master/LICENSE)
[![Codacy Badge](https://api.codacy.com/project/badge/1dec11a8c42b4d5093c035dd66635857)](https://www.codacy.com/app/yromero/py-andreani)

# py-andreani

Modulo python para comunicacion con API de [Andreani](http://www.andreani.com.ar/).
Basado en el versión 2.0 de la API

**Atención: Software en desarrollo. Aún no disponible para su uso productivo.**

## Instalación
```bash
git clone git@github.com:romeroyonatan/py-andreani.git
cd py-andreani
python setup.py install
```

## Uso
### Inicio
Instanciación de la API

* **Username**: Nombre de usuario Andreani.
* **Password**: Contraseña Andreani.
* **Cliente**: Código de cliente otorgado por comercial de Andreani.

```python
import andreani
api = andreani.API(username="eCommerce_Integra",
                   password="passw0rd",
                   cliente="ANDCORREO")
api.DEBUG = True
```

### Consultar sucursales
Devuelve una lista de sucursales Andreani habilitadas para la entrega por
mostrador. Se puede filtrar por *código postal*, *localidad* o *provincia*

```python
sucursales = api.consultar_sucursales()
sucursales = api.consultar_sucursales(codigo_postal=1001)
sucursales = api.consultar_sucursales(localidad="San Luis")
sucursales = api.consultar_sucursales(provincia="Cordoba")
```

### Cotizar envíos
Permite cotizar en línea el costo de un envío.
* **Peso**: Peso del paquete en gramos.
* **Volumen**: Volumen del paquete en cm3.
* **Contrato**: Contrato Andreani elegido (Entrega estándar, entrega urgente o
retiro en sucursal Andreani).
* **CPDestino**: Código postal del comprador.

```python
cotizacion = api.cotizar_envio(cp_destino="9410",
                               peso="1",
                               contrato="AND00EST",
                               volumen="1")
```


## Documentación oficial
Para ver la documentación oficial de Andreani, por favor descargue el documento desde [aquí](http://www.andreani.com/FilesRelated/Download?FileId=27)

