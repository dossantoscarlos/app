from django.contrib import admin

from .models.cliente import Cliente
from .models.cupom import Cupom
from .models.entrega import (
    Entrega, 
    TipoEntrega,
    TipoStatusEntrega
)
from .models.pedido import (Pedido, FormaPagamento, TipoStatusPedido)

from .models.items import Item, TipoItem
from .models.item_pedido import ItemPedido

admin.site.register(Cliente)

admin.site.register(Cupom)

admin.site.register(Entrega)
admin.site.register(TipoEntrega)
admin.site.register(TipoStatusEntrega)

admin.site.register(Pedido)
admin.site.register(TipoStatusPedido)
admin.site.register(FormaPagamento)

admin.site.register(Item)
admin.site.register(TipoItem)
admin.site.register(ItemPedido)
