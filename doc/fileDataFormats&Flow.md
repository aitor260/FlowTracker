# 📉📘 FlowTracker — Definición de Documentos y Flujo de Datos

Este documento describe los **formatos de los ficheros** y las **estructuras de datos** utilizadas en la aplicación ***FlowTracker***, así como la relación entre ellos y los **flujos de ejecución** de la aplicación.

## Índice
1. [ Documentos y estructuras de datos ](#1-documentos-y-estructuras-de-datos)
2. [ Flujo de ejecución y transición entre documentos ](#2-flujo-de-ejecución-y-transición-entre-documentos)

---

## 1. Documentos y estructuras de datos
La aplicación se basa en los siguientes documentos principales:




### 1.1. Listado de Movimientos (*input*)

#### Descripción
Este fichero contiene los registros de cada operación en una cuenta bancaría. Cada entrada en el archivo corresponde con un movimiento u operación bancaria tal y cómo se extrae del banco correspondiente. Por tanto, representa la entrada de información o *input* de la aplicación.

#### Formato
- **Tipo de fichero:** CSV (valores separados por comas)  
- **Extensión:** `.csv`  
- **Codificación recomendada:** UTF-8  

#### Campos

| Campo | Tipo Python | Descripción |
|--------|--------------|-------------|
| `fecha` | `datetime` | Día, mes y año de la operación. |
| `concepto` | `str` | Descripción o motivo del movimiento. |
| `movimiento` | `str` *(opcional)* | Tipo de movimiento (cargo, abono, transferencia...). |
| `importe` | `float` | Cantidad de dinero que se mueve (positiva o negativa). |
| `divisa` | `str` *(opcional)* | Moneda utilizada en la operación. Por defecto, EUR. |
| `disponible` | `float` | Saldo disponible tras la operación. |

#### Ejemplo

```
fecha;concepto;importe;disponible
21/10/25;Paypal;-40,99;2449,96
17/10/25;Traspaso;-203,5;2490,95
17/10/25;BONIFICACION COMISIONES;3,5;2694,45
15/10/25;FAB.NACION. DE MONEDA Y T;-3,62;2690,95
...
```

### 1.2. Cuenta Contable

#### Descripción
Documento que contiene el listado de cuentas contables definidas por el usuario. Se utiliza para asignar las cuentas debe y haber a los asientos contables.

#### Estructura de datos en Python
Para representar las cuentas contables en la aplicación se crea una clase `CuentaContable` que permita gestionar las cuentas contables, tanto las predefinidas y como aquellas definidas por el usuario, mediante la creación de objetos. Los atributos de la clase son:

| Campo | Tipo Python | Descripción |
|--------|--------------|-------------|
| `id` | `int` | Identificador único de la cuenta contable. |
| `nombre` | `str` | Nombre de la cuenta (p. ej. "Banco c/c", "Alquiler vivienda"). |
| `tipo` | `str` | Clasificación de la cuenta según su naturaleza: `"fijo"` o `"variable"`. |
| `especial` | `bool` | Indica si la cuenta forma parte del **balance** (activo, pasivo o patrimonio neto). |


#### Estructura en Python
Asimismo, una vez definida la clase que gestione las cuentas contables, se define una lista que almacene objetos de esta misma clase:

```python
cuentas: list[str]
```

#### Formato de extracción
- **Tipo de fichero:** JSON  
- **Extensión:** `.json`  
- **Codificación:** UTF-8  
- **Estructura general:** Lista de objetos JSON, uno por cuenta.

Ejemplo de una lista de Cuentas Contables exportada como JSON:

```
[
    {
        "id": 1,
        "nombre": "Banco c/c",
        "tipo": "fijo",
        "especial": true
    },
    {
        "id": 2,
        "nombre": "Efectivo",
        "tipo": "fijo",
        "especial": true
    },
    {
        "id": 3,
        "nombre": "Nomina",
        "tipo": "variable",
        "especial": false
    },
    {
        "id": 4,
        "nombre": "Alquiler",
        "tipo": "fijo",
        "especial": false
    },
    {
        "id": 5,
        "nombre": "Alimentación",
        "tipo": "variable",
        "especial": false
    },
    ...
]
```

### 1.3. Libro Diario

#### Descripción
Documento que recoge todos los asientos contables derivados de los movimientos bancarios. Cada fila representa un asiento (o parte de uno, si el movimiento implica varias cuentas).

Los asientos se crean iterando sobre los movimientos del banco y solicitando al usuario los datos contables necesarios. Por defecto, se muestran los datos que ya se tienen del movimiento (`fecha`, `concepto`, `importe`) y se pide al usuario que eliga las cuentas `debe` y `haber` correspondientes en cada caso, así como una descripción extra sobre el movimiento.

#### Estructura de datos en Python
El Libro Diario consiste en una lista (`list`) de asientos contables. Por tanto, se define una clase `AsientoContable` que permita gestionar los asientos contables mediante la creación de objetos.

```python
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

#### Formato de extracción
Alternativamente la aplicación facilita la exportación del documento como fichero de «valores separados por comas».

- **Tipo de fichero:** CSV (valores separados por comas)  
- **Extensión:** `.csv`  
- **Codificación recomendada:** UTF-8

Ejemplo de un Libro Diario exportado como fichero CSV:
```
id,fecha,concepto,debe,importeDebe,haber,importeHaber,descripcion
1,2025-10-05,PAGO ALQUILER,Alquiler,800.00,Banco c/c,400.00,Mitad del alquiler pagada por transferencia
1,2025-10-05,PAGO ALQUILER,,Efectivo,400.00,Mitad del alquiler pagada en efectivo
2,2025-10-08,REPSOL,Gasolina,65.50,Banco c/c,65.50,Recarga de gasolina del coche
3,2025-10-12,3,NOMINA MES,Banco c/c, 1800.00,Nomina,1800.00,Ingreso de la nómina del mes de octubre
4,2025-10-15,FANGALOKA,Bar/Cafeteria,45.20,Banco c/c,45.20,Cafe con Juan en Fangaloka
...
```

### 1.4. Libro Mayor
Documento que agrupa los asientos del libro diario por cuenta contable. Permite visualizar para cada cuenta su saldo total, los asientos en los que aparece (ya sea en el `debe` o en el `haber`) y los totales acumualdos de `debe` y `haber`.

#### Estructura de datos en Python
La estructura de datos optada en este caso es un diccionario anidado, ya que, permite almacenar de forma optima los datos de cada asiento y los campos adicionales para el saldo total, y los totales acumulados para el `debe` y el `haber`, y a su vez, permite exportar facilmente la estructura de datos como fichero «JSON».

```python
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

#### Formato de extracción
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

### 1.5. Cuenta de Resultados

#### Descripción
La **Cuenta de Resultados** (o cuenta de pérdidas y ganancias) muestra el resumen económico del ejercicio contable — en *FlowTracker*, **cada ejercicio corresponde siempre a un mes natural**.

Este documento se genera automáticamente a partir del **Libro Mayor**, clasificando cada cuenta según:
- El **saldo neto** (positivo → ingreso, negativo → gasto).
- Su **tipo** (`fijo` o `variable`) definido por el usuario.

El resultado final refleja el beneficio o pérdida del periodo, diferenciando entre ingresos y gastos fijos o variables.

#### Estructura de datos en Python
La estructura de datos optada en este caso es un diccionario, donde ingresos y gastos, tanto fijos como variables, tienen cada uno una entrada en el diccionario cuyo valor es otro diccionario. Este tendría como clave el nombre de la cuenta y como valor el saldo.

| Campo | Tipo Python | Descripción |
|--------|--------------|-------------|
| `periodo` | `str` | Periodo contable (formato `"YYYY-MM"`). |
| `ingresos_fijos` | `dict[str, float]` | Ingresos procedentes de cuentas fijas. |
| `ingresos_variables` | `dict[str, float]` | Ingresos procedentes de cuentas variables. |
| `gastos_fijos` | `dict[str, float]` | Gastos procedentes de cuentas fijas. |
| `gastos_variables` | `dict[str, float]` | Gastos procedentes de cuentas variables. |
| `total_ingresos_fijos` | `float` | Suma total de ingresos fijos. |
| `total_ingresos_variables` | `float` | Suma total de ingresos variables. |
| `total_ingresos` | `float` | Total de ingresos (`fijos + variables`). |
| `total_gastos_fijos` | `float` | Suma total de gastos fijos. |
| `total_gastos_variables` | `float` | Suma total de gastos variables. |
| `total_gastos` | `float` | Total de gastos (`fijos + variables`). |
| `resultado` | `float` | Beneficio o pérdida (`total_ingresos - total_gastos`). |

#### Formato de extracción
Al trabajar con diccionarios la idea de cara a exportar la Cuenta de Resultados es trabajar directamente con «JSON».

- **Tipo de fichero**: JSON (JavaScript Object Notation)
- **Extensión**: `.json`

Ejemplo de Cuenta de Resultados exportada como fichero JSON:
```json
{
    "periodo": "2025-10",
    "ingresos_fijos": {
        "Nomina": 1500.00
    },
    "ingresos_variables": {
        "Intereses": 5.00
    },
    "gastos_fijos": {
        "Alquiler": 700.00,
        "Suscripciones": 50.00
    },
    "gastos_variables": {
        "Supermercado": 220.00,
        "Ocio": 85.00
    },
    "total_ingresos_fijos": 1500.00,
    "total_ingresos_variables": 5.00,
    "total_ingresos": 1505.00,
    "total_gastos_fijos": 750.00,
    "total_gastos_variables": 305.00,
    "total_gastos": 1055.00,
    "resultado": 450.00
}
```
---

## 2. Flujo de ejecución y transición entre documentos

El flujo general de la aplicación se divide en **dos fases principales**: una **fase interactiva** de registro contable y una **fase automatizada** de procesamiento y generación de resultados.

> [!NOTE]
> Se asume que el usuario ha definido previamente todas las cuentas que considere oportunas para utilizar la aplicación con un ejercicio personal.

### Fase 1: Creación interactiva del Libro Diario

#### Objetivo  
Registrar y clasificar manualmente cada movimiento bancario en forma de asientos contables, con ayuda del usuario, para generar el Libro Diario.

#### Entrada
- Fichero «CSV» con el listado de movimientos bancarios descargado desde el banco.  
- Fichero «JSON» con las cuentas contables definidas por el usuario (`cuentas.json`).

#### Proceso
1. Se lee el *JSON* con las cuentas contables del usuario y se crean objetos `CuentaContable`.
2. Se lee el *CSV* de movimientos.
3. Para cada movimiento, la aplicación solicita al usuario:
   - Cuentas **Debe** y **Haber** afectadas.
   - Importe correspondiente a cada una (en caso necesario).
   - Descripción adicional.
4. Con esta información, se genera un documento *CSV* de salida `libro_diario.csv` como último paso de la fase.

#### Salida
- `libro_diario.csv` (o formato JSON si se desea mayor trazabilidad).  

Esta fase requiere de intervención manual y puede ejecutarse de forma progresiva. Su resultado servirá como punto de partida para la fase automatizada.

---
### Fase 2: Generación automatizada de resultados

#### Objetivo
Calcular automáticamente los documentos derivados (Libro Mayor y Cuenta de Resultados) a partir de un Libro Diario previamente creado.

#### Entrada 
- `libro_diario.csv` (generado en la Fase 1).  
- `cuentas.json` (definido previamente por el usuario).

#### Proceso
1. Se importa el fichero *JSON* de cuentas contables y se crean objetos `CuentaContable`.
2. Se itera sobre el Libro Diario (fichero *CSV* generado en la primera fase de ejecución del programa) y por cada línea se crea un objeto `AsientoContable` que se almacena en una lista `libroDiario`.
3. Se agrupan los asientos por cuenta para calcular el **Libro Mayor** en forma de diccionario, generando un documento intermedio *JSON* de salida (`libro_mayor.json`).
4. Se analizan los saldos de cada cuenta, clasificando los movimientos como **ingresos** o **gastos**, y como **fijos** o **variables** según corresponda.  
4. Se crea la **Cuenta de Resultados** en forma de diccionario y a su vez se genera un documento *JSON* de salida (`cuenta_resultados.json`), que refleja un resumen del ejercicio.

#### Salida
- `libro_mayor.json`.  
- `cuenta_resultados.json`.

Esta fase crea un documento (a partir del Libro Diario) que resume, de forma mensual, todos los ingresos y gastos clasificados por tipo y calcula automáticamente el resultado del ejercicio (beneficio o pérdida). Todos los cálculos se realizan de forma automática sin requerir de interacción adicional por parte del usuario.
