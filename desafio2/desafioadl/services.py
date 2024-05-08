from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    """
    Recupera todas las tareas y subtareas existentes en la base de datos.
    
    Returns:
        (QuerySet, QuerySet): Un par de objetos QuerySet, uno para tareas y otro para subtareas.
    Descripción:
    Un QuerySet en Django es una lista de objetos que cumplen ciertas condiciones, obtenidos
    a través de una consulta a la base de datos. Es una forma de interactuar con la base de datos
    de manera eficiente y flexible, ya que permite filtrar, ordenar y manipular los datos de forma
    sencilla y rápida.
    """
    tareas = Tarea.objects.all()
    subtareas = SubTarea.objects.all()
    return tareas, subtareas
def crear_nueva_tarea(descripcion):
    """
    Crea una nueva tarea con la descripción dada y la guarda en la base de datos.

    Args:
        descripcion (str): Descripción de la nueva tarea.

    Returns:
        (QuerySet, QuerySet): Un par de objetos QuerySet, uno para tareas y otro para subtareas después de la inserción.
    """
    tarea = Tarea(descripcion=descripcion)
    tarea.save()
    return Tarea.objects.all(), SubTarea.objects.all()

def crear_sub_tarea(id_tarea, descripcion):
    """ Crea una nueva sub-tarea relacionada con la tarea dada y la guarda en la base de datos
    Args: 
        id_tarea(int): ID de la tarea a la que se asociara la sub tarea
        descripcion(str): Descripcion de la nueva sub-tarea
    Returns:
         (QuerySet, QuerySet): Un par de objetos QuerySet, uno para tareas y otro para subtareas después de la inserción."""
    tarea = Tarea.objects.get(id=id_tarea)
    sub_tarea = SubTarea(tarea=tarea, descripcion=descripcion)
    sub_tarea.save()
    return Tarea.objects.all(), SubTarea.objects.all()

def elimina_tarea(id_tarea):
    """
    Elimina una tarea y todas sus sub-tareas de la base de datos.

    Args:
        id_tarea (int): ID de la tarea a eliminar.

    Returns:
        (QuerySet, QuerySet): Un par de objetos QuerySet, uno para tareas y otro para subtareas después de la eliminación.
    """
    tarea = Tarea.objects.get(id=id_tarea)
    tarea.delete()
    return Tarea.objects.all(), SubTarea.objects.all()

def elimina_sub_tarea(id_subtarea):
    """
    Elimina una sub-tarea de la base de datos.

    Args:
        id_subtarea (int): ID de la sub-tarea a eliminar.

    Returns:
        (QuerySet, QuerySet): Un par de objetos QuerySet, uno para tareas y otro para subtareas después de la eliminación.
    """
    sub_tarea = SubTarea.objects.get(id=id_subtarea)
    sub_tarea.delete()
    return Tarea.objects.all(), SubTarea.objects.all()

def imprimir_en_pantalla(tareas, subtareas):
    """
    Imprime las tareas y subtareas en la pantalla de manera ordenada.

    Args:
        tareas (QuerySet): QuerySet de tareas.
        subtareas (QuerySet): QuerySet de subtareas.
    """
    for tarea in tareas:
        print(f"[{tarea.id}]{tarea.descripcion}")
        for sub_tarea in subtareas.filter(tarea=tarea):
            print(f"....[{sub_tarea.id}]{sub_tarea.descripcion}")

    