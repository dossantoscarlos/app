from django.contrib import admin

from .models.cliente import Cliente
from .models.cupom import Cupom
from .models.entrega import (
    Entrega, 
    TipoEntrega,
    TipoStatusEntrega
)
from .models.pedido import (Pedido, FormaPagamento, TipoStatusPedido)



admin.site.register(Cliente)

admin.site.register(Cupom)

admin.site.register(Entrega)
admin.site.register(TipoEntrega)
admin.site.register(TipoStatusEntrega)

admin.site.register(Pedido)
admin.site.register(TipoStatusPedido)
admin.site.register(FormaPagamento)


