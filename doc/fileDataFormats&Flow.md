# 📉📘 FlowTracker — Definición de Documentos y Flujo de Datos

Este documento describe los **formatos de los ficheros** y las **estructuras de datos** utilizadas en la aplicación ***FlowTracker***, así como la relación entre ellos.  

La aplicación se basa en las siguientes etapas principales:
1. **Listado de movimientos**: lectura del CSV bancario.
2. **Libro diario**: generación de asientos contables.
3. **Libro mayor**: agrupación de los asientos por cuenta contable.
4. **Cuenta de resultados**: TBD

---

## 1. Listado de Movimientos (*input*)

### Descripción
Este fichero contiene los registros de cada operación en una cuenta bancaría. Cada entrada en el archivo corresponde con un movimiento u operación bancaria tal y cómo se extrae del banco correspondiente. Por tanto, representa la entrada de información o *input* de la aplicación.

### Formato
- **Tipo de fichero:** CSV (valores separados por comas)  
- **Extensión:** `.csv`  
- **Codificación recomendada:** UTF-8  

### Campos

| Campo | Tipo Python | Descripción |
|--------|--------------|-------------|
| `fecha` | `datetime` | Día, mes y año de la operación. |
| `concepto` | `str` | Descripción o motivo del movimiento. |
| `movimiento` | `str` *(opcional)* | Tipo de movimiento (cargo, abono, transferencia...). |
| `importe` | `float` | Cantidad de dinero que se mueve (positiva o negativa). |
| `divisa` | `str` *(opcional)* | Moneda utilizada en la operación. Por defecto, EUR. |
| `disponible` | `float` | Saldo disponible tras la operación. |

### Ejemplo

```
fecha;concepto;importe;disponible
21/10/25;Paypal;-40,99;2449,96
17/10/25;Traspaso;-203,5;2490,95
17/10/25;BONIFICACION COMISIONES;3,5;2694,45
15/10/25;FAB.NACION. DE MONEDA Y T;-3,62;2690,95
...
```

## 2. Cuenta Contable

### Descripción
Documento que contiene el listado de cuentas contables definidas por el usuario. Se utiliza para asignar las cuentas debe y haber a los asientos contables.

### Formato
- **Tipo de fichero**: texto plano
- **Extensión**: `.txt`

### Ejemplo
Ejemplo del contenido de un fichero de texto plano que almacena las cuentas contables:
```
Banco c/c
Gasolina
Supermercados
Bar/Cafeteria
Restaurantes
...
```

### Estructura en Python
```
cuentas: list[str]
```

> [!IMPORTANT]
> ***TBD** - Hay que elegir con un fichero `.txt` con los nombres de las cuentas es suficiente para trabajar o queremos optar por un «JSON» en su lugar para poder almacenar más metadatos por cada cuenta.*

## 3. Libro Diario

### Descripción
Documento que recoge todos los asientos contables derivados de los movimientos bancarios. Cada fila representa un asiento (o parte de uno, si el movimiento implica varias cuentas).

Los asientos se crean iterando sobre los movimientos del banco y solicitando al usuario los datos contables necesarios. Por defecto, se muestran los datos que ya se tienen del movimiento (`fecha`, `concepto`, `importe`) y se pide al usuario que eliga las cuentas `debe` y `haber` correspondientes en cada caso, así como una descripción extra sobre el movimiento.

### Estructura de datos en Python
El Libro Diario consiste en una lista (`list`) de asientos contables. Por tanto, se define una clase `AsientoContable` que permita gestionar los asientos contables mediante la creación de objetos.

```
libroDiario: list[AsientoContable]
```

Los atributos de la clase son los siguientes:

| Campo | Tipo Python | Descripción |
| ----- | ----------- | ----------- |
| `id` | `int` | Identificador del asiento contable. Puede repetirse si un movimiento tiene varios asientos asociados. |
| `fecha` | `datetime` | Fecha efectiva del movimiento. |
| `concepto` | `str` | Motivo del movimiento (procedente del CSV bancario). |
| `debe` | `str` | Cuenta a la que se carga el importe (recibe el valor). |
| `importeDebe` | `float` | Importe cargado en la cuenta DEBE. |
| `haber` | `str` | Cuenta que abona el importe (de donde sale el dinero). |
| `importeHaber` | `float` | Importe cargado en la cuenta HABER. |
| `descripcion` | `str` | Comentario opcional que contextualiza el movimiento. |

### Formato de extracción
Alternativamente la aplicación facilita la exportación del documento como fichero de «valores separados por comas».

- **Tipo de fichero:** CSV (valores separados por comas)  
- **Extensión:** `.csv`  
- **Codificación recomendada:** UTF-8

Ejemplo de un Libro Diario exportado como fichero CSV:
```
id,fecha,concepto,debe,importeDebe,haber,importeHaber,descripcion
1,2025-10-05,PAGO ALQUILER,Alquiler,800.00,Banco c/c,400.00,Mitad del alquiler pagada por transferencia
1,2025-10-05,PAGO ALQUILER,,0.00,Efectivo,400.00,Mitad del alquiler pagada en efectivo
2,2025-10-08,REPSOL,Gasolina,65.50,Banco c/c,65.50,Recarga de gasolina del coche
3,2025-10-12,3,NOMINA MES,Banco c/c, 1800.00,Nomina,1800.00,Ingreso de la nómina del mes de octubre
4,2025-10-15,FANGALOKA,Bar/Cafeteria,45.20,Banco c/c,45.20,Cafe con Juan en Fangaloka
...
```

## 4. Libro Mayor
Documento que agrupa los asientos del libro diario por cuenta contable. Permite visualizar para cada cuenta su saldo total, los asientos en los que aparece (ya sea en el `debe` o en el `haber`) y los totales acumualdos de `debe` y `haber`.

### Estructura de datos en Python
La estructura de datos optada en este caso es un diccionario anidado, ya que, permite almacenar de forma optima los datos de cada asiento y los campos adicionales para el saldo total, y los totales acumulados para el `debe` y el `haber`, y a su vez, permite exportar facilmente la estructura de datos como fichero «JSON».

```
libroMayor: dict[str, dict[str, Any]]
```

Donde cada clave es el nombre de una cuenta y el valor es un diccionario con la siguiente estructura:
```
{
    "asientos": list[int],          # IDs de los asientos asociados a esta cuenta
    "debe_total": float,            # Total acumulado en el debe
    "haber_total": float,           # Total acumulado en el haber
    "saldo": float                  # Resultado (debe_total - haber_total)
}
```

> [!IMPORTANT]
> ***TBD** - Hay que elegir si en el array de `asientos` guardar los objetos de la clase `AsientoContable` o si almacenar solamente los `id`s.*

### Formato de extracción
Al trabajar con diccionarios la idea de cara a exportar el Libro Mayor es trabajar directamente con «JSON».

- **Tipo de fichero**: JSON (JavaScript Object Notation)
- **Extensión**: `.json`

Ejemplo de un Libro Mayor exportado como fichero JSON:
```
{
    "Banco c/c": {
        "asientos": [1, 3, 4],
        "debe_total": 2500.00,
        "haber_total": 2200.00,
        "saldo": 300.00
    },
    "Restaurantes": {
        "asientos": [2],
        "debe_total": 100.00,
        "haber_total": 200.00,
        "saldo": -100.00
    },
    ...
}
```

## 4. Cuenta de resultados
**TBD**

---

## Flujo de transición entre documentos

El flujo de trabajo en **FlowTracker** sigue las siguientes etapas:

```
[ CSV de movimientos bancarios ]
          │
          ▼
 Lectura y parsing (fila a fila)
          │
          ▼
[ Libro Diario ] (Creación de objetos AsientoContable mediante interacción con el usuario)
          │
          ▼
 Agrupación por cuenta
          │
          ▼
[ Libro Mayor ] (Cálculo de totales y saldos por cuenta)
```

> [!NOTE]
> Se asume que el usuario ha definido previamente todas las cuentas que considere oportunas para utilizar la aplicación con un ejercicio personal.

### 1.	Listado de movimientos
1. Se importa el documento `.txt` que contiene las cuentas definidas previamente por el usuario.
2. Se importa el documento `.csv` exportado desde el banco y se procesa línea por línea. Para cada línea se muestra los datos al usuario y se espera a que este introduzca las cuentas DEBE y HABER y una descripción. Cada registro puede originar uno o varios asientos contables (en caso de ser más de uno, todos ellos están asociados entre sí con un mismo `id`) y se guardan en forma de objeto de la clase `AsientoContable`.

### 2.	Libro diario
El conjunto de asientos en forma de objetos `AsientoContable` se guarda en una lista y, adicionalmente/opcionalmente, en un fichero «CSV» intermedio.

### 3.	Libro mayor
Se crea un diccionario donde la clave sea un `str` correspondiente a cada uno de los elementos de la lista de cuentas contables y el valor sea un diccionario para los campos `asientos`, `debe_total`, `haber_total` y `saldo`. Se itera sobre el libro diario (lista de asientos contables) y se realizan las siguientes acciones:

1. Añadir el `id` del asiento a la lista para la clave `asientos`. 
2. Sumar acumulativamente el importe a la cuenta correspondiente (DEBE o HABER).
3. Calcular el saldo total restante para esa cuenta mediante la diferencia.

Se exporta (opcionalmente) a JSON para su fácil lectura y posterior análisis.