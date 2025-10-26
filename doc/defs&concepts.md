# Definiciones y conceptos básicos de contabilidad 💶

A continuación, se recogen las definiciones y conceptos básicos de contabilidad relacionados al funcionamiento de la aplicación [FlowTracker](../README.md).

## Movimiento bancario

Registro de una operación en una cuenta bancaría. Se relaciona estrechamente con el activo frecuencia de Cuenta corriente bancaria (Banco c/c).

Recoge información acerca de la fecha, concepto, importe, tipo de movimiento —cargo o abono—.

## Asiento contable

Toda creación o modificación de un activo o un pasivo se convierte en un asiento contable. 

> [!NOTE]
> El caso de la aplicación [FlowTracker](../README.md), cada movimiento de Banco c/c se traducirá en un asiento contable.

Un asiento contable es una entrada del libro diario que recoge información en una o varias líneas en qué cuenta se carga el movimiento (debe) y en que cuenta se abona (haber).

*Por ejemplo, para reflejar el movimiento de «Pago alquiler» se carga el gasto en la cuenta «Gastos de viviendo» y abano en «Banco c/c».*

## Libro diario

El libro diario es el documento que recoge, ordenados por fecha, todos los asientos contables de un periodo, denominado comunmente como «*ejercicio*».

>[!NOTE]
> En el caso de la aplicación de [FlowTracker](../README.md), el ejercicio se considera un mes.

Cada asiento contable contiene:
- **ID**: identificador de asiento.
- **Fecha**: fecha en la que se hizo efectivo el movimiento.
- **Concepto**: concepto del movimiento. Un título que recogela causa del movimiento.
- **Cuenta de cargo o DEBE**: es la cuenta en la que se carga el movimiento, es decir, la cuenta que recibe el ingreso o se carga el gasto.
- **Importe cuenta DEBE**: es el valor del importe que se carga en la cuenta DEBE.
- **Cuenta de abono o HABER**: es la cuenta en la que abona el movimiento, es decir, la cuenta de la que recoge el importe a cargar.
- **Importe HABER**: es el valor del importe que se carga en la cuenta HABER.
- **Descripción**: breve texto que contexualiza el porqué del movimiento que se recoge en forma de asiento.

>[!NOTE]
> Un movimiento u operación bancaria puede involucrar a su vez múltiples cuentas «DEBE» o «HABER». En estos casos, se reflejarían dos o más asientos en el libro diario, todos ellos con el mismo «ID».

## Cuenta

Una **cuenta contable** es un registro individual donde se agrupan todos las operaciones relacionadas con un mismo concepto o elemento del patrimonio.

Ejemplos de cuentas son: *banco, alquiler, ventas, gastos de alimentación, etc.*

Una cuenta sirve para registrar y controlar cómo cambian los distintos elementos del patrimonio *(p.ej. dinero, deudas, ingresos, gastos, etc.)* a lo largo del tiempo.

Si un elemento del patrimonio no se registra como cuenta, su evolución no será estudiable.

## Libro mayor

Documento que agrupa todos los movimientos organizado por cuentas. 

*Por ejemplo, refleja todos los cambios que ha sufrido la cuenta «Gastos en alimentación». Mostrará todos los asientos donde aparece, ya sea en el «DEBE» o en el «HABER», y su saldo acumulado.*

## Cuenta de resultados

Es el resumen final del ejercicio, donde se muestran los ingresos y los gastos durante ese periodo de tiempo. La conclusión es el resultado del ejercicio.

Si el resultado del ejercicio es positivo, el ejercicio habrá generado beneficios y, en consecuencia, un aumento del patrimonio. En caso contrario, el ejercicio habrá generados más gastos que ingresos, lo que supone una reducción del patrimonio.

Típicamente, se suele diferenciar entre:

- **Gastos e ingresos FIJOS**: entradas recurrentes, presentes en todas las «Cuentas de Resultados» y cuyo valor es similar en cada ejercicio.
- **Gastos e ingresos VARIABLES**: entradas no recurrentes y cuyos valores son aleatorios para cada ejercicio.

## Balance de situación

El **balance de situación** es un documento contable que muestra la situación económica y financiera de una empresa o personal **en un momento determinado**.

Se estructura en dos grandes partes:

- **Activo**: lo que la empresa o persona posee *(p. ej. bienes materiales, bienes inmuebles, derechos, dinero en efectivo o en banco, etc.)*

>[!NOTE]
> Un derecho se considera un pasivo que un tércero tiene con la empresa propia o con uno mismo. Es el derecho a cobrarase una deuda agena.

- **Pasivo y Patrimonio Neto**: lo que la empresa debe *(p. ej. deudas, obligaciones, etc.)* y el capital propio, respectivamente.

>[!NOTE]
> El **Patrimonio Neto** (PN) representa la parte de los recursos de la empresa o persona que pertenece a sus propietarios, una vez resueltas todas las deudas *(el pasivo)*.

>[!NOTE]
> Dentro del «PN», en el contexto empresarial, se incluye el **capital propio**, que es el dinero o bienes que los socios o propietarios han aportado al iniciar o financiar la empresa. Además del capital, el «PN» puede incluir **reservas** *(beneficio acumulado de ejercicios anteriores)* o **resultado del ejercicio** *(beneficio o pérdida del periodo considerado)*.

El balance presenta de forma ordenada todas las cuentas del activo, pasivo y patrimonio, mostrando el valor total de lo que la empresa tiene y debe.

Se basa en el siguiente principio.

```
ACTIVOS = PASIVOS + PATRIMONIO NETO
```