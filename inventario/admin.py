from django.contrib import admin

# Importar modelos de Inventario
from .models import Producto
from .models import Material
from .models import DetalleProductosMaterial
from .models import MovimientoInventarioMaterial
from .models import MovimientoInventarioProduto

# Registrar modelos para que aparescan en interfaz de administracion
admin.site.register(Producto)
admin.site.register(Material)
admin.site.register(DetalleProductosMaterial)
admin.site.register(MovimientoInventarioMaterial)
admin.site.register(MovimientoInventarioProduto)