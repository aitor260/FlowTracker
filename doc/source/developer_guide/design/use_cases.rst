Casos de Uso
============

El **diagrama de Casos de Uso** de FlowTracker ``v1.0`` recoge todas las interacciones que el **Usuario final** puede realizar. El sistema contempla un único actor, reflejando la naturaleza local de la aplicación, y organiza las funcionalidades en **cuatro** grandes categorías.

La **gestión de ejercicios** permite crear, cargar y guardar Ejercicios. La **gestión de Planes Contables** (PC) cubre la creación, consulta y eliminación de Planes Contables. El **tratamiento de movimientos** es el núcleo de la aplicación: permite al usuario importar movimiento bancarios semi-automáticamente o de forma manual. Y, por último, la **consulta de informes** ofrece acceso a diferentes documentos contables como el Libro Diario, Libro Mayor o Cuenta de Resultados. 

.. figure:: ../images/DiagramaCasosUso.svg
   :alt: Diagrama de Casos de Uso

   Figura 1: Diagrama de Casos de Uso

Categoría A. Gestión de Ejercicios
----------------------------------

FlowTracker es un programa que gestiona la contabilidad a través de proyectos de contabilidad, denominados «*Ejercicios*». Esta primera versión del programa comtempla la funcionalidad básica de gestión de proyectos, permitiendo a los usuarios realizar las siguientes operaciones sobre un Ejercicio:

* **A1. Crear un Ejercicio**: iniciar un nuevo proyecto de contabilidad.
* **A2. Cargar un Ejercicio**: abrir un Ejercicio existente para trabajar con él.
* **A3. Guardar un Ejercicio**: persistir el estado del Ejercicio en el disco duro.

.. warning::
    En esta versión ``v1.0`` de FlowTracker no se han implementado los Casos de Uso para *Eliminar un Ejercicio* o *Modificar las propiedades de un Ejercicio*, dejando su implementación para futuras versiones.

Categoría B. Gestión de Planes y Cuentas Contables
--------------------------------------------------


.. important::
    Cada Ejercicio en FlowTracker debe esta asociado a un Plan Contable.

A diferencia de los entornos corporativos y legales, donde es obligatorio el uso del PGC del Estado, FlowTracker está diseñado para una contabilidad a nivel personal y simplificada. Por lo tanto, el sistema permite a los usuarios diseñar y utilizar Planes Contables personalizados.

Para optimizar la definición y reutilización de las cuentas, los Planes Contables son entidades independientes que pueden ser asociados a múltiples Ejercicios.

Al mismo tiempo, varios Planes Contables pueden contener varías Cuentas Contables en común, por lo que también se facilita la reutilización de las Cuentas Contables generandolas como entidades independiente de los Planes Contables.

El usuario dispone de las siguientes funcionalidades para la gestión de Planes y Cuentas Contables:

* **B1. Crear un Plan Contable**: establecer una nueva estructura de cuentas.
* **B2. Consultar un Plan Contable**: visualizar la estructura de cuentas definida.
* **B3. Borrar un Plan Contable**: borrar una estructura de cuentas existente.
* **B4. Crear una Cuenta Contable**: establecer una nueva cuenta.
* **B5. Borrar una Cuenta Contable**: eliminar una cuenta existente. Se borrará de todos los Planes Contables en los que se encuentre.

Categoría C. Uso del Ejercicio: gestión de asientos contables
-------------------------------------------------------------

Para el trascurso normal de un Ejercicio, es necesario poder añadir asientos contables al Libro Diario. En esta primera versión de FlowTracker, se han establecido dos métodos para ello:

* Añadir un asiento contable manualmente.
* Añadir un asiento contable a partir de un archivo CSV que contenga los movimientos bancarios de una cuenta corriente de una entidad bancaria.

Por tanto, los casos de uso nesarios para gestionar los asientos contables son:

* **C1. Registrar un asiento contable manualmente**: introduciendo la información de forma manual mediante un cuestionario se introduce un nuevo asiento contable en el Libro Diario.
* **C2. Importar movimientos bancarios**: se selecciona un fichero CSV que contiene los movimientos bancarios de una cuenta corriente de una entidad bancaria. Este acción desencadena los siguientes:
    * **C2.1. Conciliar movimiento bancarios**: movimiento a movimiento, se recorre la lista de movimientos y se añade información adicional básica y adicional para la generación del asiento en el Libro Diario.
    * **C2.2. Registrar asiento contable**: se registra el asiento contable en el Libro Diario, de acuerdo a la información aportada en el paso anterior.
* **C3. Eliminar manualmente un asiento contable**: se elimina un asiento contable del Libro Diario.

La lista de asientos contables puede ser más o menos larga. Por tanto, puede ser que se desee guardar el proyecto durante el proceso de conciliación de movimientos bancarios. En tal caso, es necesario persistir el estas del Ejercicio para poder retomar la conciliación más adelante, al cargar de nuevo el proyecto.

Al mismo tiempo, se tiene que poder mover de forma manual por la lista de movimiento para añadir un asiento concreto, entre todos los que contenga el fichero CSV fuente.

Categoría D. Resultados del Ejercicio: gestión de informes
-----------------------------------------------------------

Por último, el objetivo esencial de la aplicación FlowTracke es generar informes contables. Por lo tanto, se debe poder:

* **D1. Consultar el libro diario**: contiene conciliados todos los movimientos bancarios y otras acciones contables. Registra todos los movimientos sufrido durante el Ejercicio en forma de asientos.
* **D2. Consultar el libro mayor**: contiene el resumen de los movimientos sufridos durante el Ejercicio, organizados por Cuentas Contables.
* **D3. Consultar el balance de pérdidas y ganancias**: contiene el análisis de las Cuentas Contables de tipo Nominal, es decir, Cuentas que están asociadas a Gastos e Ingresos.

.. warning::
    La aplicación está orientada a poder implementar, en próximas versiones, la consulta del Balance de situación para tener la capacidad de contemplar la representación de informes relacionados con Cuentas Contables de tipo *Especial*, es decir, Cuentas que están asociadas a Activos, Pasivos y Patrimonio.
