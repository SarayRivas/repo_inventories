
from rest_framework import viewsets
from .models import Inventory
from .serializers import InventorySerializer
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse




class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all().order_by('id_inventory')
    serializer_class = InventorySerializer


    
@require_http_methods(["GET", "HEAD"])
def health_check(request):

    res = JsonResponse({"status": "ok"})
    return _no_store(res)
