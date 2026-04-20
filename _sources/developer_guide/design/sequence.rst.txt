Secuencias
==========

Categoria B. Gestión de Planes y Cuentas Contables
--------------------------------------------------

Secuencia B1. Crear un Plan Contable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El flujo de ejecución para la creación de un nuevo Plan Contable comienza con la introducción del comando ``flowtracker plan create -n <nombre_plan>`` por parte del Usuario final en la terminal. A continuación, la interfaz CLI delega la petición al ``ui/controller.py`` mediante el método ``request_plan_creation()``.

El Controlador actúa como puente hacia la capa ``core`` e invoca el método ``create_new_plan()`` del módulo ``core/plan/actions.py``. Este asume la responsabilidad de la creación e instancia en memoria una nueva entidad a partir del modelo ``PlanContable``, definido en ``core/plan/models.py``.

Una vez creado el objeto, el módulo ``core/plan/actions.py`` invoca al método ``save_plan()`` del módulo ``data/manager.py``, que se encarga de guardar el nuevo Plan Contable en el disco duro para persistirlo de forma definitiva.

Tras la confirmación de guardado ``is_saved``, ``core/plan/actions.py`` devuelve el objeto completo al Controlador. Esto asegura que las capas superiores trabajen con los datos finales consolidados por el sistema. Finalmente, el controlador informa a la CLI del éxito de la operación mediante un mensaje ``success_status``. Tras la recepción de este mensaje, se renderiza en pantalla el mensaje ``Plan created successfully``.

.. figure:: ../images/B1_sequence.svg
    :align: center
    :width: 100%
