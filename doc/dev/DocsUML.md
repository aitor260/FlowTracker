# Documentación UML

Para planificar el desarrollo de esta aplicación se han realizado los siguientes diagramas UML.

## Diagrama de casos de uso

El diagrama de casos de uso muestra los diferentes casos de uso de la aplicación. Es el punto de partida para el desarrollo de la aplicación. Es importante definir los casos de uso antes de comenzar a codificar la aplicación. De esta forma se define el alcance y resultado de la aplicación, en este primer desarrollo.

Para el desarrollo de FlowTracker se han considerado los casos de uso que se muestran en el siguiente diagrama de casos de uso.

![Diagrama de casos de uso](diagrams/DiagramaCasosUso.drawio.svg)

Los 16 casos de uso que se muestran en el diagrama, se pueden agrupar en 4 categorías:

### Categoría 1. Gestión de Ejercicios

FlowTracker es un programa que gestiona la contabilidad a través de proyectos de contabilidad, denominados «*Ejercicios*». Esta primera versión del programa comtempla la funcionalidad básica de gestión de proyectos, permitiendo a los usuarios realizar las siguientes operaciones sobre un Ejercicio:

- **Crear un Ejercicio**: iniciar un nuevo proyecto de contabilidad.
- **Cargar un Ejercicio**: abrir un Ejercicio existente para trabajar con él.
- **Guardar un Ejercicio**: persistir el estado del Ejercicio en el disco duro.

> [!NOTE]
> En esta versión inicial de FlowTracker, los casos de uso para *Eliminar un Ejercicio* o *Modificar las propiedades de un Ejercicio*, no están contemplados.

### Categoría 2. Gestión de Planes y Cuentas Contables

Cada Ejercicio en FlowTracker debe esta asociado a un Plan Contable.

A diferencia de los entornos corporativos y legales, donde es obligatorio el uso del PGC del Estado, FlowTracker está diseñado para una contabilidad a nivel personal y simplificada. Por lo tanto, el sistema permite a los usuarios diseñar y utilizar Planes Contables personalizados.

Para optimizar la definición y reutilización de las cuentas, los Planes Contables son entidades independientes que pueden ser asociados a múltiples Ejercicios.

Al mismo tiempo, varios Planes Contables pueden contener varías Cuentas Contables en común, por lo que también se facilita la reutilización de las Cuentas Contables generandolas como entidades independiente de los Planes Contables.

El usuario dispone de las siguientes funcionalidades para la gestión de Planes y Cuentas Contables:

- **Crear un Plan Contable**: establecer una nueva estructura de cuentas.
- **Consultar un Plan Contable**: visualizar la estructura de cuentas definida.
- **Borrar un Plan Contable**: borrar una estructura de cuentas existente.
- **Crear una Cuenta Contable**: establecer una nueva cuenta.
- **Borrar una Cuenta Contable**: eliminar una cuenta existente. Se borrará de todos los Planes Contables en los que se encuentre.

### 3. Uso del Ejercicio: gestión de asientos contables

Para el trascurso normal de un Ejercicio, es necesario poder añadir  asientos contables al Libro Diario. En esta primera versión de FlowTracker, se han establecido dos métodos para ello:

- Añadir un asiento contable manualmente.
- Añadir un asiento contable a partir de un archivo CSV que contenga los movimientos bancarios de una cuenta corriente de una entidad bancaria.

Por tanto, los casos de uso nesarios para gestionar los asientos contables son:

- **Registrar un asiento contable manualmente**: introduciendo la información de forma manual mediante un cuestionario se introduce un nuevo asiento contable en el Libro Diario.
- **Importar movimientos bancarios**: se selecciona un fichero CSV que contiene los movimientos bancarios de una cuenta corriente de una entidad bancaria. Este acción desencadena los siguientes:
    - **Conciliar movimiento bancarios**: movimiento a movimiento, se recorre la lista de movimientos y se añade información adicional básica y adicional para la generación del asiento en el Libro Diario.
    - **Registrar asiento contable**: se registra el asiento contable en el Libro Diario, de acuerdo a la información aportada en el paso anterior.
- **Eliminar manualmente un asiento contable**: se elimina un asiento contable del Libro Diario.

La lista de asientos contables puede ser más o menos larga. Por tanto, puede ser que se desee guardar el proyecto durante el proceso de conciliación de movimientos bancarios. En tal caso, es necesario persistir el estas del Ejercicio para poder retomar la conciliación más adelante, al cargar de nuevo el proyecto.

Al mismo tiempo, se tiene que poder mover de forma manual por la lista de movimiento para añadir un asiento concreto, entre todos los que contenga el fichero CSV fuente.

### 4. Resultados del Ejercicio: gestión de informes

Por último, el objetivo esencial de la aplicación FlowTracke es generar informes contables. Por lo tanto, se debe poder:

- **Consultar el libro diario**: contiene conciliados todos los movimientos bancarios y otras acciones contables. Registra todos los movimientos sufrido durante el Ejercicio en forma de asientos.
- **Consultar el libro mayor**: contiene el resumen de los movimientos sufridos durante el Ejercicio, organizados por Cuentas Contables.
- **Consultar el balance de pérdidas y ganancias**: contiene el análisis de las Cuentas Contables de tipo Nominal, es decir, Cuentas que están asociadas a Gastos e Ingresos.

La aplicación está orientada a poder implementar, en próximas versiones, la consulta del *Balance de situación* para tener la capacidad de contemplar la representación de informes relacionados con Cuentas Contables de tipo Real, es decir, Cuentas que están asociadas a Activos, Pasivos y Patrimonio.

## Diagrama de secuencia

## Diagrama de clases

A continuación, se muestra el diagrama de clases que representa la estructura de la aplicación.



![Diagrama de clases](diagrams/DiagramaClases.drawio.svg)