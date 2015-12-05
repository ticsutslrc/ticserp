# -*- coding: utf-8 -*-
from django.db import models

# Representa los tipos posibles de movimientos de inventario
TIPO_MOVIMIENTO_ENTRADA = 1
TIPO_MOVIMIENTO_SALIDA = 2
TIPO_MOVIMIENTO_REMISION = 3
TIPO_MOVIMIENTO_AJUSTE = 4

TIPOS_MOVIMIENTO_INVENTARIO = (
    (TIPO_MOVIMIENTO_ENTRADA, 'Entrada'),
    (TIPO_MOVIMIENTO_SALIDA, 'Salida'),
    (TIPO_MOVIMIENTO_REMISION, 'Remision'),
    (TIPO_MOVIMIENTO_AJUSTE, 'Ajuste'),
)


# Create your models here.
class Producto(models.Model):
    """
    Modelo Producto. Este modelo representa el producto terminado que se compone de varios inventario.models.Material
    el detalle de este producto se encuentra en la clase
    """

    # Campos generales
    nombre = models.CharField(null=False, max_length=30, db_index=True)
    descripccion = models.CharField(null=True, blank=True, max_length=60)
    numero_inventario = models.CharField(null=False, max_length=10, db_index=True)
    codigo_barras = models.CharField(max_length=20, default='', blank=True, db_index=True)
    peso = models.PositiveIntegerField(default=0)

    # Campos para controlar costos
    ultimo_costo = models.DecimalField(max_digits=10, decimal_places=4)
    costo_promedio = models.DecimalField(max_digits=10, decimal_places=4)

    # Campos para manejar stock
    cantidad_total_almacen = models.IntegerField(default=0)
    cantidad_minimo_almacen = models.PositiveIntegerField(default=5)

    # Para guardar cualquier comentario que fuese necesario
    comentarios = models.TextField(blank=True)

    # Campos de control de fecha
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_index=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        """
        Define la salida en string de este modelo
        """
        return '<Producto> Nombre: {0} Stock: {1} Costo: {2}'.format(
            self.nombre.encode('utf8'),
            self.cantidad_total_almacen,
            self.ultimo_costo,
        )

    class Meta:
        ordering = ['-fecha_modificacion']

    def salida_inventario(self, cantidad, comentarios="N/A"):
        """
        Genera la salida de productos de inventario, Afecta el stock y ademas genera los movimientos en las tablas
        correspondientes, el campo comentarios es opcional regresa el nuevo MovimientoInventarioProduto generado

        Ejemplo:

        >>> producto = Producto.objects.get(pk=1)
        >>> print producto.salida_inventario(10, comentarios="Hola esta salida es de luis iturrios")

        """
        # Revisar que el tipo de cantidad sea entero si no mandar Exception
        assert type(cantidad) is int
        # Revisar que la cantidad super el zero si no mandar Exception
        if cantidad <= 0:
            # lanzar Exception
            raise Exception('Al realizar un movimiento en inventario la cantidad debe de ser mayor a zero')

        # calcular la cantidad que quedara en stock despues del movimiento
        cantidad_total_despues = self.cantidad_total_almacen - cantidad

        # Instanciar el nuevo movimiento
        movimiento = MovimientoInventarioProduto()
        # guardar el tipo de movimiento
        movimiento.tipo = TIPO_MOVIMIENTO_SALIDA
        # Asiganar el movimiento a este producto
        movimiento.producto = self
        # Guardar la cantidad del movimiento
        movimiento.cantidad = cantidad
        # guardar la cantidad total de almacen antes
        movimiento.cantidad_total_almacen_antes = self.cantidad_total_almacen
        # Guardar la cantidad que quedara despues del movimiento
        movimiento.cantidad_total_almacen_despues = cantidad_total_despues
        # Revisar si se enviaron comentarios
        if str(comentarios).strip():
            # si se enviaron comentarios asignar
            movimiento.comentarios = comentarios
        # Guardar movimiento en base de datos
        movimiento.save()
        # afectar el stock general
        self.cantidad_total_almacen = cantidad_total_despues
        # guardar el stock general en base de datos
        self.save()
        # regresar el movimiento
        return movimiento

    def entrada_inventario(self, cantidad, comentarios="N/A"):
        """
        Genera la entrada de productos de inventario, Afecta el stock y ademas genera los movimientos en las tablas
        correspondientes, el campo comentarios es opcional regresa el nuevo MovimientoInventarioProduto generado

        Ejemplo:

        >>> producto = Producto.objects.get(pk=1)
        >>> print producto.entrada_inventario(10, comentarios="Hola esta entrada es de luis iturrios")

        """
        # Revisar que el tipo de cantidad sea entero si no mandar Exception
        assert type(cantidad) is int
        # Revisar que la cantidad super el zero si no mandar Exception
        if cantidad <= 0:
            # lanzar Exception
            raise Exception('Al realizar un movimiento en inventario la cantidad debe de ser mayor a zero')

        # calcular la cantidad que quedara en stock despues del movimiento
        cantidad_total_despues = self.cantidad_total_almacen + cantidad

        # Instanciar el nuevo movimiento
        movimiento = MovimientoInventarioProduto()
        # guardar el tipo de movimiento
        movimiento.tipo = TIPO_MOVIMIENTO_ENTRADA
        # Asiganar el movimiento a este producto
        movimiento.producto = self
        # Guardar la cantidad del movimiento
        movimiento.cantidad = cantidad
        # guardar la cantidad total de almacen antes
        movimiento.cantidad_total_almacen_antes = self.cantidad_total_almacen
        # Guardar la cantidad que quedara despues del movimiento
        movimiento.cantidad_total_almacen_despues = cantidad_total_despues
        # Revisar si se enviaron comentarios
        if str(comentarios).strip():
            # si se enviaron comentarios asignar
            movimiento.comentarios = comentarios
        # Guardar movimiento en base de datos
        movimiento.save()
        # afectar el stock general
        self.cantidad_total_almacen = cantidad_total_despues
        # guardar el stock general en base de datos
        self.save()
        # regresar el movimiento
        return movimiento

    def remision_inventario(self, cantidad, comentarios="N/A"):
        """
        Genera la remision de productos de inventario, Afecta el stock y ademas genera los movimientos en las tablas
        correspondientes, el campo comentarios es opcional regresa el nuevo MovimientoInventarioProduto generado

        Ejemplo:

        >>> producto = Producto.objects.get(pk=1)
        >>> print producto.remision_inventario(10, comentarios="Hola esta remision es de luis iturrios")

        """
        # Revisar que el tipo de cantidad sea entero si no mandar Exception
        assert type(cantidad) is int
        # Revisar que la cantidad super el zero si no mandar Exception
        if cantidad <= 0:
            # lanzar Exception
            raise Exception('Al realizar un movimiento en inventario la cantidad debe de ser mayor a zero')

        # calcular la cantidad que quedara en stock despues del movimiento
        cantidad_total_despues = self.cantidad_total_almacen - cantidad

        # Instanciar el nuevo movimiento
        movimiento = MovimientoInventarioProduto()
        # guardar el tipo de movimiento
        movimiento.tipo = TIPO_MOVIMIENTO_REMISION
        # Asiganar el movimiento a este producto
        movimiento.producto = self
        # Guardar la cantidad del movimiento
        movimiento.cantidad = cantidad
        # guardar la cantidad total de almacen antes
        movimiento.cantidad_total_almacen_antes = self.cantidad_total_almacen
        # Guardar la cantidad que quedara despues del movimiento
        movimiento.cantidad_total_almacen_despues = cantidad_total_despues
        # Revisar si se enviaron comentarios
        if str(comentarios).strip():
            # si se enviaron comentarios asignar
            movimiento.comentarios = comentarios
        # Guardar movimiento en base de datos
        movimiento.save()
        # afectar el stock general
        self.cantidad_total_almacen = cantidad_total_despues
        # guardar el stock general en base de datos
        self.save()
        # regresar el movimiento
        return movimiento

    def ajuste_inventario(self, cantidad, comentarios="N/A"):
        """
        Genera la ajuste de productos de inventario, Afecta el stock y ademas genera los movimientos en las tablas
        correspondientes, el campo comentarios es opcional regresa el nuevo MovimientoInventarioProduto generado

        Ejemplo:

        >>> producto = Producto.objects.get(pk=1)
        >>> print producto.ajuste_inventario(10, comentarios="Hola este ajuste es de luis iturrios")

        """
        # Revisar que el tipo de cantidad sea entero si no mandar Exception
        assert type(cantidad) is int
        # Revisar que la cantidad super el zero si no mandar Exception
        if cantidad <= 0:
            # lanzar Exception
            raise Exception('Al realizar un movimiento en inventario la cantidad debe de ser mayor a zero')

        # calcular la cantidad que quedara en stock despues del movimiento
        cantidad_total_despues = cantidad

        # Instanciar el nuevo movimiento
        movimiento = MovimientoInventarioProduto()
        # guardar el tipo de movimiento
        movimiento.tipo = TIPO_MOVIMIENTO_AJUSTE
        # Asiganar el movimiento a este producto
        movimiento.producto = self
        # Guardar la cantidad del movimiento
        movimiento.cantidad = cantidad
        # guardar la cantidad total de almacen antes
        movimiento.cantidad_total_almacen_antes = self.cantidad_total_almacen
        # Guardar la cantidad que quedara despues del movimiento
        movimiento.cantidad_total_almacen_despues = cantidad_total_despues
        # Revisar si se enviaron comentarios
        if str(comentarios).strip():
            # si se enviaron comentarios asignar
            movimiento.comentarios = comentarios
        # Guardar movimiento en base de datos
        movimiento.save()
        # afectar el stock general
        self.cantidad_total_almacen = cantidad_total_despues
        # guardar el stock general en base de datos
        self.save()
        # regresar el movimiento
        return movimiento


class Material(models.Model):
    """
    Modelo Material. Este modelo contiene las deficiones de materiales (Materia Prima) necesarios para la fabricacion
    de cada inventario.models.Producto ademas mentariene el stock en almacen
    """
    # Campos generales
    nombre = models.CharField(null=False, max_length=30, db_index=True)
    descripccion = models.CharField(null=True, blank=True, max_length=60)
    numero_inventario = models.CharField(null=False, max_length=10, db_index=True)
    codigo_barras = models.CharField(max_length=20, default='', blank=True, db_index=True)
    peso = models.PositiveIntegerField()

    # Campos para controlar costos
    ultimo_costo = models.DecimalField(max_digits=10, decimal_places=4)
    costo_promedio = models.DecimalField(max_digits=10, decimal_places=4)

    # Campos para manejar stock
    cantidad_total_almacen = models.IntegerField(default=0)
    cantidad_minimo_almacen = models.PositiveIntegerField(default=5)

    # Campos de relacion con proveedor
    # proveedor = models.ForeignKey('compras.Proveedor', null=False)

    # Para guardar cualquier comentario que fuese necesario
    comentarios = models.TextField(blank=True)

    # Campos de control de fecha
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_index=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        """
        Define la salida en string de este modelo
        """
        return '<Material> Nombre: {0} Stock: {1} Costo: {2} Proveedor: '.format(
            self.nombre.encode('utf8'),
            self.cantidad_total_almacen,
            self.ultimo_costo,
            #self.proveedor.nombre,
        )

    class Meta:
        ordering = ['-fecha_modificacion']

    def salida_inventario(self, cantidad, comentarios="N/A"):
        """
        Genera la salida de material de inventario,
        Afecta el stock y ademas genera los movimientos en las tablas correspondientes, el campo comentarios es opcional
        regresa el nuevo MovimientoInventarioMaterial generado

        Ejemplo:

        >>> material = Material.objects.get(pk=1)
        >>> print material.salida_inventario(10, comentarios="Hola esta salida es de luis iturrios")

        """
        # Revisar que el tipo de cantidad sea entero si no mandar Exception
        assert type(cantidad) is int
        # Revisar que la cantidad super el zero si no mandar Exception
        if cantidad <= 0:
            raise Exception('Al realizar un movimiento en inventario la cantidad debe de ser mayor a zero')

        # calcular la cantidad que quedara en stock despues del movimiento
        cantidad_total_despues = self.cantidad_total_almacen - cantidad

        # Instanciar el nuevo movimiento
        movimiento = MovimientoInventarioMaterial()
        # guardar el tipo de movimiento
        movimiento.tipo = TIPO_MOVIMIENTO_SALIDA
        # Asiganar el movimiento a este material
        movimiento.material = self
        # Guardar la cantidad del movimiento
        movimiento.cantidad = cantidad
        # guardar la cantidad total de almacen antes
        movimiento.cantidad_total_almacen_antes = self.cantidad_total_almacen
        # Guardar la cantidad que quedara despues del movimiento
        movimiento.cantidad_total_almacen_despues = cantidad_total_despues
        # Revisar si se enviaron comentarios
        if str(comentarios).strip():
            # si se enviaron comentarios asignar
            movimiento.comentarios = comentarios
        # Guardar movimiento en base de datos
        movimiento.save()
        # afectar el stock general
        self.cantidad_total_almacen = cantidad_total_despues
        # guardar el stock general en base de datos
        self.save()
        # regresar el movimiento
        return movimiento

    def entrada_inventario(self, cantidad, comentarios="N/A"):
        """
        Genera la entrada de material de inventario,
        Afecta el stock y ademas genera los movimientos en las tablas correspondientes, el campo comentarios es opcional
        regresa el nuevo MovimientoInventarioMaterial generado

        Ejemplo:

        >>> material = Material.objects.get(pk=1)
        >>> print material.entrada_inventario(10, comentarios="Hola esta entrada es de luis iturrios")

        """
        # Revisar que el tipo de cantidad sea entero si no mandar Exception
        assert type(cantidad) is int
        # Revisar que la cantidad super el zero si no mandar Exception
        if cantidad <= 0:
            raise Exception('Al realizar un movimiento en inventario la cantidad debe de ser mayor a zero')

        # calcular la cantidad que quedara en stock despues del movimiento
        cantidad_total_despues = self.cantidad_total_almacen + cantidad

        # Instanciar el nuevo movimiento
        movimiento = MovimientoInventarioMaterial()
        # guardar el tipo de movimiento
        movimiento.tipo = TIPO_MOVIMIENTO_ENTRADA
        # Asiganar el movimiento a este material
        movimiento.material = self
        # Guardar la cantidad del movimiento
        movimiento.cantidad = cantidad
        # guardar la cantidad total de almacen antes
        movimiento.cantidad_total_almacen_antes = self.cantidad_total_almacen
        # Guardar la cantidad que quedara despues del movimiento
        movimiento.cantidad_total_almacen_despues = cantidad_total_despues
        # Revisar si se enviaron comentarios
        if str(comentarios).strip():
            # si se enviaron comentarios asignar
            movimiento.comentarios = comentarios
        # Guardar movimiento en base de datos
        movimiento.save()
        # afectar el stock general
        self.cantidad_total_almacen = cantidad_total_despues
        # guardar el stock general en base de datos
        self.save()
        # regresar el movimiento
        return movimiento

    def remision_inventario(self, cantidad, comentarios="N/A"):
        """
        Genera la remision de material de inventario,
        Afecta el stock y ademas genera los movimientos en las tablas correspondientes, el campo comentarios es opcional
        regresa el nuevo MovimientoInventarioMaterial generado

        Ejemplo:

        >>> material = Material.objects.get(pk=1)
        >>> print material.remision_inventario(10, comentarios="Hola esta remision es de luis iturrios")

        """
        # Revisar que el tipo de cantidad sea entero si no mandar Exception
        assert type(cantidad) is int
        # Revisar que la cantidad super el zero si no mandar Exception
        if cantidad <= 0:
            raise Exception('Al realizar un movimiento en inventario la cantidad debe de ser mayor a zero')

        # calcular la cantidad que quedara en stock despues del movimiento
        cantidad_total_despues = self.cantidad_total_almacen - cantidad

        # Instanciar el nuevo movimiento
        movimiento = MovimientoInventarioMaterial()
        # guardar el tipo de movimiento
        movimiento.tipo = TIPO_MOVIMIENTO_REMISION
        # Asiganar el movimiento a este material
        movimiento.material = self
        # Guardar la cantidad del movimiento
        movimiento.cantidad = cantidad
        # guardar la cantidad total de almacen antes
        movimiento.cantidad_total_almacen_antes = self.cantidad_total_almacen
        # Guardar la cantidad que quedara despues del movimiento
        movimiento.cantidad_total_almacen_despues = cantidad_total_despues
        # Revisar si se enviaron comentarios
        if str(comentarios).strip():
            # si se enviaron comentarios asignar
            movimiento.comentarios = comentarios
        # Guardar movimiento en base de datos
        movimiento.save()
        # afectar el stock general
        self.cantidad_total_almacen = cantidad_total_despues
        # guardar el stock general en base de datos
        self.save()
        # regresar el movimiento
        return movimiento

    def ajuste_inventario(self, cantidad, comentarios="N/A"):
        """
        Genera la ajuste de material de inventario,
        Afecta el stock y ademas genera los movimientos en las tablas correspondientes, el campo comentarios es opcional
        regresa el nuevo MovimientoInventarioMaterial generado

        Ejemplo:

        >>> material = Material.objects.get(pk=1)
        >>> print material.ajuste_inventario(10, comentarios="Hola esta remision es de luis iturrios")

        """
        # Revisar que el tipo de cantidad sea entero si no mandar Exception
        assert type(cantidad) is int
        # Revisar que la cantidad super el zero si no mandar Exception
        if cantidad <= 0:
            raise Exception('Al realizar un movimiento en inventario la cantidad debe de ser mayor a zero')

        # calcular la cantidad que quedara en stock despues del movimiento
        cantidad_total_despues = cantidad

        # Instanciar el nuevo movimiento
        movimiento = MovimientoInventarioMaterial()
        # guardar el tipo de movimiento
        movimiento.tipo = TIPO_MOVIMIENTO_AJUSTE
        # Asiganar el movimiento a este material
        movimiento.material = self
        # Guardar la cantidad del movimiento
        movimiento.cantidad = cantidad
        # guardar la cantidad total de almacen antes
        movimiento.cantidad_total_almacen_antes = self.cantidad_total_almacen
        # Guardar la cantidad que quedara despues del movimiento
        movimiento.cantidad_total_almacen_despues = cantidad_total_despues
        # Revisar si se enviaron comentarios
        if str(comentarios).strip():
            # si se enviaron comentarios asignar
            movimiento.comentarios = comentarios
        # Guardar movimiento en base de datos
        movimiento.save()
        # afectar el stock general
        self.cantidad_total_almacen = cantidad_total_despues
        # guardar el stock general en base de datos
        self.save()
        # regresar el movimiento
        return movimiento


class DetalleProductosMaterial(models.Model):
    """
    Modelo DetalleProductosMaterial. Este modelo contiene el detalle de que material requiere que producto y
    cuantos de cada uno
    """

    # Relacion indica que producto pertenece este detalle
    producto = models.ForeignKey(Producto, null=False)
    # Relacion indica que material requiere este producto
    material = models.ForeignKey(Material, null=False)
    # Indica la cantidad de material que requiere cada proucto para ser fabricado
    cantidad = models.PositiveIntegerField(default=0)
    # Para guardar cualquier comentario que fuese necesario
    comentarios = models.TextField(blank=True)

    # Campos de control de fecha
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_index=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        """
        Define la salida en string de este modelo
        """
        return '<DetalleProductosMaterial> Producto: {0} Material: {1} Cantidad: {2} Comentarios: {3}'.format(
            self.producto.nombre.encode('utf8'),
            self.material.nombre.encode('utf8'),
            self.cantidad,
            self.comentarios.encode('utf8'),
        )

    class Meta:
        ordering = ['-fecha_modificacion']


class MovimientoInventarioProduto(models.Model):
    """
    Modelo MovimientoInventarioProduto. Este modelo contiene los movimientos de inventario que se generaron a
    determinado producto. Producto tiene un metodo para generar este movimiento.
    """
    # Relacion con producto
    producto = models.ForeignKey(Producto, null=False)
    # Indica la cantidad por la que se genero este movimiento
    cantidad = models.IntegerField(default=0)
    # Indica la cantidad que existia en stock antes de este movimiento
    cantidad_total_almacen_antes = models.IntegerField(default=0)
    # Indica la cantidad que existe en stock despues de este movimiento
    cantidad_total_almacen_despues = models.IntegerField(default=0)
    # Indica que tipo de movimiento fue. Este para saber si descontar o aumentar el stock
    tipo = models.PositiveIntegerField(default=1, choices=TIPOS_MOVIMIENTO_INVENTARIO)
    # Para guardar cualquier comentario que fuese necesario
    comentarios = models.TextField(blank=True)

    # Campos de control de fecha
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_index=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        """
        Define la salida en string de este modelo
        """
        return '<MovimientoInventarioProduto> Producto: {0} Tipo: {1} Cantidad: {2} Comentarios: {3}'.format(
            self.producto.nombre.encode('utf8'),
            self.get_tipo_display().encode('utf8'),
            self.cantidad,
            self.comentarios.encode('utf8'),
        )

    class Meta:
        ordering = ['-fecha_modificacion']


class MovimientoInventarioMaterial(models.Model):
    """
    Modelo MovimientoInventarioMaterial. Este modelo contiene los movimientos de inventario que se generaron a
    determinado material. Material tiene un metodo para generar este movimiento.
    """
    # Relacion con material
    material = models.ForeignKey(Material, null=False)
    # Indica la cantidad por la que se genero este movimiento
    cantidad = models.IntegerField(default=0)
    # Indica la cantidad que existia en stock antes de este movimiento
    cantidad_total_almacen_antes = models.IntegerField(default=0)
    # Indica la cantidad que existe en stock despues de este movimiento
    cantidad_total_almacen_despues = models.IntegerField(default=0)
    # Indica que tipo de movimiento fue. Este para saber si descontar o aumentar el stock
    tipo = models.PositiveIntegerField(default=1, choices=TIPOS_MOVIMIENTO_INVENTARIO)
    # Para guardar cualquier comentario que fuese necesario
    comentarios = models.TextField(blank=True)

    # Campos de control de fecha
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_index=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        """
        Define la salida en string de este modelo
        """
        return '<MovimientoInventarioMaterial> Material: {0} Tipo: {1} Cantidad: {2} Comentarios: {3}'.format(
            self.material.nombre.encode('utf8'),
            self.get_tipo_display().encode('utf8'),
            self.cantidad,
            self.comentarios.encode('utf8'),
        )

    class Meta:
        ordering = ['-fecha_modificacion']
