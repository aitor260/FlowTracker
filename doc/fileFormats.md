# Definición del formato de cada fichero
A continuación se especifican y definen cada uno de los ficheros o estructuras de datos, tanto entradas o *inputs* como salidas u *outputs*, así como el tipo de archivo o estructura de datos y el formato del contenido, es decir, los campos que contiene cada uno y el tipo de dato en Python.

## 1. Listado de movimientos bancarios
Este fichero contiene los registros de cada operación en una cuenta bancaría. Cada entrada en el archivo corresponde con un movimiento u operación bancaria tal y cómo se extrae del banco correspondiente. Por tanto, representa la entrada de información o *input* de la aplicación.

Por defecto, el tipo de documento será de **«valores separados por comas»** (con extensión .csv) y contendrá los siguientes campos por cada fila:

- **`fecha`**: día, mes y año en que se realizó la operación. (`datetime`)
- **`concepto`**: descripción o motivo que acompaña a la transferencia de dinero. (`string`)
- ***`movimiento`***: especifica el tipo de movimiento realizado. *No se requiere.* (`string`)
- **`importe`**: cantidad de dinero que se mueve en una operación. (`float`)
- ***`divisa`***: se refiere a la moneda utilizada en la operación (por defecto, euro). *No se requiere.* (`string`)
- **`disponible`**: saldo posterior a la operación. (`float`)

Ejemplo del contenido de un fichero «.csv» que almacena los movimientos extraidos del banco:
```
fecha;concepto;importe;disponible
21/10/25;Paypal;-40,99;2449,96
17/10/25;Traspaso;-203,5;2490,95
17/10/25;BONIFICACION COMISIONES;3,5;2694,45
15/10/25;FAB.NACION. DE MONEDA Y T;-3,62;2690,95
```

Este listado se importará a la aplicación usando el módulo `csv` de Python que itera sobre cada línea del documento de entrada, pedirá al usuario que confirme e introduzca los datos adicionales para crear asientos contables mediante una clase `asientoContable`.

## 2. Cuenta contable
La estructura de datos para definir y almacenar las cuentas contables será un **fichero de texto plano** con extensión «.txt» donde cada línea contendrá el nombre de una cuenta.

La idea es cargar todas las líneas del documento para obtener en la memoria de la aplicación un array de tipo `string` que contenga los nombres de las cuentas contables definidas por el usuario. Este documento se podrá alterar a través de la aplicación tanto para añadir, modificar o eliminar elementos.

Ejemplo del contenido de un fichero de texto plano que almacena las cuentas contables:
```
Banco
Gasolina
Supermercado
Bar/Cafeteria
Bizum
```

## 3. Asiento contable
Esta estructura representa la unidad fundamental de la contabilidad de partida doble. Se genera de forma interactiva a partir de la **clase `AsientoContable`** y se almacena temporalmente en una lista de objetos antes de convertirse en el Libro Diario, un `DataFrame` de la librería *pandas*.

Los campos de datos de esta estructura de datos o atributos de la clase son:
- **`id`**: identificador de asiento. (`int`)
- **`fecha`**: fecha en la que se hizo efectivo el movimiento. (`datetime`)
- **`concepto`**: descripción o título del movimiento que recoge el motivo. (`string`)
- **`debe`**: la cuenta en la que se carga el movimiento, es decir, la cuenta que recibe el ingreso o se carga el gasto. Se determina interactuando con el usuario. (`string`)
- **`importeDebe`**: el valor del importe que se carga en la cuenta DEBE. (`float`)
- **`haber`**: la cuenta en la que abona el movimiento, es decir, la cuenta de la que recoge el importe a cargar. Se determina interactuando con el usuario. (`string`)
- **`importeHaber`**: el valor del importe que se carga en la cuenta HABER. (`float`)
- **`descripcion`**: breve texto que contexualiza el porqué del movimiento que se recoge en forma de asiento. Introducido a mano por el usuario. (`string`)

>[!NOTE]
> Un movimiento u operación bancaria puede involucrar a su vez múltiples cuentas `debe` o `haber`. En estos casos, se reflejarían dos o más objetos de `AsientoContable`, todos ellos con el mismo `id`.

## 4. Libro diario
Esta estructura de datos recoge, ordenados por fecha, todos los asientos contables de un ejercicio. Se construye a partir del «listado de movimientos bancarios» iterando entre cada una de las entradas de este para generar un listado de asientos como salida.

El tipo de documento será inicialmente un **array de objetos `AsientoContable`** y posteriormente un **`DataFrame`** de la librería *pandas*, que contenga por cada fila un asiento contable con los campos definidos arriba como columnas, y ordenados por la columna `fecha`.

Ejemplo de un 'DataFrame` para el libro diario de un ejercicio:
```
+----+------+------------+-----------------+---------------+---------------+---------+----------------+-------------------------------------------+
|    |   id | fecha      | concepto        | debe          |   importeDebe | haber   |   importeHaber | descripcion                               |
|----+------+------------+-----------------+---------------+---------------+---------+----------------+-------------------------------------------|
|  0 |    1 | 2025-10-15 | Pago Repsol     | Gasolina      |          65.5 | Banco   |           65.5 | Recarga de gasolina del coche             |
|  1 |    2 | 2025-10-16 | Pago Cena Amigo | Bizum         |          35   | Banco   |           35   | Bizum a Aitor de la cena                  |
|  2 |    3 | 2025-10-17 | Nómina Mensual  | Banco         |        1800   | Nomina  |         1800   | Ingreso de la nómina del mes de octubre   |
|  3 |    4 | 2025-10-18 | Mercadona       | Supermercado  |          78.9 | Banco   |           78.9 | Compra barbacoa sábado en casa de Paula   |
|  4 |    5 | 2025-10-19 | Desayuno Bar    | Bar/Cafetería |           5.8 | Banco   |            5.8 | Desayuno en cafetería cerca de la oficina |
|  5 |    6 | 2025-10-24 | Recibo de Bizum | Banco         |          15   | Bizum   |           15   | Bizum de Sara por pintxos                 |
|  6 |    7 | 2025-10-25 | Fangaloka       | Bar/Cafetería |          45.2 | Banco   |           45.2 | Café con Juan                             |
+----+------+------------+-----------------+---------------+---------------+---------+----------------+-------------------------------------------+
```

> [!NOTE]
> ***TBD*** *Opcionalmente, la aplicación permitirá exportar este documento como fichero del tipo «valores separados por comas».*

## 5. Libro mayor

Estoy un poco atascado con esta parte. Me gustaría poder ver tus ejemplos de Excel para acordarme mejor de cómo deberían verse el Libro Diario y el Libro Mayor.
