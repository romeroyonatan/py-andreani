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

### Para ansiosos

#### Lo que hace el comprador
```python
>>> import andreani
>>> api = andreani.API(username="eCommerce_Integra",
...                    password="passw0rd",
...                    cliente="ANDCORREO")
>>> api.DEBUG = True
>>> # comprador consulta sucursales disponibles para retirar
>>> api.consultar_sucursales(localidad="San Justo")
[{'tipo_telefono': None,
  'direccion': Pte. Peron 3368 , 1754 , SAN JUSTO , BUENOS AIRES,
  'longitud': None,
  'sucursal': 20,
  'tipo_sucursal': 3,
  'descripcion': SAN JUSTO,
  'responsable': None,
  'telefono': None,
  'resumen': SAN JUSTO,
  'numero': SJU,
  'mail': None,
  'horade_trabajo': None,
  'latitud': None
 },
 {'tipo_telefono': None,
  'direccion': Urquiza 2958 , 3000 , SANTA FE , SANTA FE,
  'longitud': None,
  'sucursal': 55,
  'tipo_sucursal': 2,
  'descripcion': SANTA FE,
  'responsable': None,
  'telefono': None,
  'resumen': SANTA FE,
  'numero': SFN,
  'mail': None,
  'horade_trabajo': None,
  'latitud': None
}]
>>> # comprador cotiza el envio del paquete
>>> api.cotizar_envio(sucursal_retiro=20,
...                   cp_destino="1754",
...                   peso="1000",
...                   contrato="AND00SUC",
...                   volumen="1000")
{'peso_aforado': 1000.0,
 'tarifa': 25.41,
 'categoria_distancia': LOCAL,
 'categoria_peso': 2,
 'categoria_peso_id': 2,
 'categoria_distancia_id': 1
}
>>> # comprador confirma la compra e ingresa datos de envio
>>> api.confirmar_compra(
...     sucursal_retiro=20,
...     provincia="Buenos Aires",
...     localidad="San Justo",
...     codigo_postal=1754,
...     calle="Florencio Varela",
...     numero="1903",
...     nombre_apellido="Elsa Pato",
...     tipo_documento="DNI",
...     numero_documento="12345678",
...     email="email@example.com",
...     numero_celular="1515151111",
...     numero_telefono="43211234",
...     detalle_productos_entrega="Prueba de entrega",
...     detalle_productos_retiro="Prueba de envio",
...     peso=1000,
...     volumen=1000,
...     contrato="AND00SUC",
...     tarifa=25.41,
... )
{'recibo': None, 'numero_andreani': *00000000255574}
```


#### Lo que hace el vendedor

```python
>>> import andreani
>>> api = andreani.API(username="eCommerce_Integra",
...                    password="passw0rd",
...                    cliente="ANDCORREO")
>>> api.DEBUG = True
>>> # vendedor consulta ventas para imprimir etiquetas (en modo debug puede tardar mucho)
>>> api.reporte_envios_pendientes_impresion()
[{
  'departamento': None,
  'detalle_productosa_entregar': None,
  'nombrey_apellido': asd,
  'localidad': 11 DE SEPTIEMBRE,
  'numero_andreani': *00000010311000,
  'provincia': BUENOS AIRES,
  'piso': None,
  'calle': Bme. Mitre,
  'numero': 1668
},{
  'departamento': 3,
  'detalle_productosa_entregar': zapatos magicos,
  'nombrey_apellido': Diaz Arce Facundo,
  'localidad': 11 DE SEPTIEMBRE,
  'numero_andreani': *00000000081332,
  'provincia': BUENOS AIRES,
  'piso': 1,
  'calle': calle 1,
  'numero': 1111
}]
>>> # vendedor selecciona una venta y obtiene pdf de la etiqueta para imprimir
>>> api.imprimir_constancia("*00000010311000")
https://www.e-andreani.com/CasaStaging/ecommerce/impresionetiquetas/ImpresionEti
quetas.aspx?data=zuAo9XN8yRPx54aZyfFLH6V23cMdt22pgWDZPg73LIRTRSYaQ%2b6pj%2f3Oala
IzQ2bmZVH0sFoRnsXP9uAZ2hIls01KEZvOBrvD309r2EHdGYpGJBCxeb%2bp3y7AKP7AMi1ydRzmoZg0
kWGQ0EH8f3sDpmNsVxJNM8G2eveqUIOA4CJXImxMRFoMEMT7McwlvT%2bTlGrdYjqSlL7RSUdXUlUst0
cyEYsNG1zRQtCdEUFJlqDoaLjz3PlhVW6iz3zvgkLh%2fh9ZFchdQngMDo2c4i6tXrkafzYf4CEF3rT0
NPOSoMF%2b%2fcZnOpeTNEvMz9r41M0UcAd6o%2b0AbzlbXbj5ulGBu0zzKfRa0qie679SmfftL14ghD
92QEkRuAQgz4RRLY26hQv5Dke8u3SSdS8t%2b%2bLGPu2uLXFERRsLpZvtsVsF95dXYE0SU2sPGC78Un
0HeV7Y6vh%2bKQ3t2E%3d
>>> # vendedor consulta ventas para enviar a andreani
>>> api.reporte_envios_pendientes_ingreso()
[{
 'departamento': None,
 'detalle_productosa_entregar': None,
 'nombrey_apellido': Fernando Ramos,
 'localidad': 11 DE SEPTIEMBRE,
 'numero_andreani': *00000010248630,
 'provincia': BUENOS AIRES,
 'piso': None,
 'calle': Corrientes,
 'numero': 777
}]
>>> # vendedor selecciona piezas e imprime remito de imposicion
>>> api.generar_remito_imposicion("*00000000255574")
{
 'entidades': {
    'string': [*00000010248630]
 },
 'remitode_imposicion': CONT02999RIM0000000000009310,
 'pdf': https://www.e-andreani.com/CasaStaging/ecommerce/impresionetiquetas/Impr
 esionEtiquetas.aspx?data=zuAo9XN8yRPx54aZyfFLH6V23cMdt22pgWDZPg73LIRTRSYaQ%2b6p
 j%2f3OalaIzQ2bmZVH0sFoRnsXP9uAZ2hIls01KEZvOBrvD309r2EHdGYpGJBCxeb%2bp3y7AKP7AMi
 1ydRzmoZg0kWGQ0EH8f3sDpmNsVxJNM8G2eveqUIOA4CJXImxMRFoMEMT7McwlvT%2bTlGrdYjqSlL7
 RSUdXUlUsicaCKVcE6j6SX%2bIiSESsBJn9wthDx0jKK2WTmUWSCXvci%2fTh2CKVPLniZ9lVLiWXNs
 iwhNPvoFvjDkQul9YJN1zNhf7WykrxI3cSJEvKHx1X8LANMWzdtaGYsZfnMlGuIa4GwKKGXpgInEJ99
 OD%2bItOentDCquVzL7LkzFwMnXvi%2b8bdRceXmjVeFgzxtrx3HxxydLXxiIhAKZfo3NM0L5w%2fk%
 2fCENWsAMWz8FxJeUbtVhpuJdpWcsLlhS2sX%2btiJQ%3d%3d
}
```

### Inicio

Instanciación de la API

* **Username**: Nombre de usuario Andreani.
* **Password**: Contraseña Andreani.
* **Cliente**: Código de cliente otorgado por comercial de Andreani.

Todos estos datos serán dados por su comercial Andreani.

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

### Confirmar compra
Genera un envío en Andreani.

Asigna un identificador con el cual se va a hacer el seguimiento.
Luego se debe llamar al WS de Imprimir Constancia para finalizar el
proceso de Alta del envío.

* **sucursal_retiro**: Código de "Sucursal Andreani" donde el
envío permanecerá en Custodia. Obligatorio
para los Servicios de Retiro en Sucursal
(valor "sucursal" de la consulta de
sucursales)
* **provincia**
* **localidad**
* **codigo_postal**
* **calle**
* **numero**
* **departamento**
* **piso**
* **nombre_apellido**
* **tipo_documento**
* **numero_documento**
* **email**
* **numero_celular**
* **numero_telefono**
* **nombre_apellido_alternativo**
* **numero_transaccion**: ID de identificación de envío del Cliente
* **detalle_productos_entrega**
* **detalle_productos_retiro**
* **peso**: Expresado en Gramos (gr.)
* **volumen**: Expresado en Centímetros Cúbicos (cc3.) (No es
obligatorio si se usan categorías de peso).
Considerar el volumen del envoltorio/Embalaje.
valor_declarado -- Float: Obligatorio para los Servicios que incluye
seguro en caso de siniestro
* **valor_cobrar**: Obligatorio para los Servicio que incluyen
Gestión Cobranza (pago contrareembolso)
* **sucursal_cliente**: Nombre que identifica la sucursal/depósito
del Cliente. Obligatorio para los Servicios
de Retiro en Sucursal Andreani más próxima
a la sucursal/depósito de Cliente
* **categoria_distancia**: Código de categoría para la cotización.
Obligatorio cuando la tarifas del
servicio se cotizan por Categorías de
Distancia
* **categoria_facturacion**: Uso interno
* **categoria_peso**: Código de categoría para la cotización.
Obligatorio cuando la tarifas del servicio
se cotizan por Categorías de Peso. (por ej.
1.- Zapatos, 2.-Indumentaria)
* **tarifa**: Valor de cotización del envío. Sólo se setea
si se consume el servicio web de Cotización.
Este valor es de referencia, ya que el sistema
recalculará la tarifa junto con el alta.

```python
>>> api.confirmar_compra(
...     sucursal_retiro=20,
...     provincia="Buenos Aires",
...     localidad="San Justo",
...     codigo_postal=1754,
...     calle="Florencio Varela",
...     numero="1903",
...     nombre_apellido="Elsa Pato",
...     tipo_documento="DNI",
...     numero_documento="12345678",
...     email="email@example.com",
...     numero_celular="1515151111",
...     numero_telefono="43211234",
...     detalle_productos_entrega="Prueba de entrega",
...     detalle_productos_retiro="Prueba de envio",
...     peso=1000,
...     volumen=1000,
...     contrato="AND00SUC",
...     tarifa=25.41,
... )
```

## Documentación oficial
Para ver la documentación oficial de Andreani, por favor descargue el documento desde [aquí](http://www.andreani.com/FilesRelated/Download?FileId=27)

