from django.utils import timezone
from rest_framework import viewsets
from .models import Product, Warehouse, Shelve, Inventory, InventoryMovement, WarehouseCreation, OrderCreation, AuditLog 
from .serializers import AuditLogSerializer, InventorySerializer, ProductSerializer, WarehouseSerializer, ShelveSerializer, InventoryMovementSerializer, WarehouseCreationSerializer, OrderCreationSerializer
from django.db import transaction, DatabaseError
from django.db.utils import OperationalError
from django.db.models import F
from rest_framework.exceptions import ValidationError
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.cache import cache
from rest_framework import request
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response




class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all().order_by('id_inventory')
    serializer_class = InventorySerializer


    
@require_http_methods(["GET", "HEAD"])
def health_check(request):

    res = JsonResponse({"status": "ok"})
    return _no_store(res)
