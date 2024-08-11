import json
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from core.models import Order, Laundry
from .serializers import OrderSerializer
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt, csrf_protect
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,logout, login,get_user_model
from django.contrib.auth.models import User
from django.utils import timezone
import uuid


User = get_user_model()


@api_view(['POST'])
@ensure_csrf_cookie
@permission_classes([IsAuthenticated])
def create_pickup_order(request):
    if request.method == 'POST':
        current_user = request.user
        if current_user.is_authenticated:
            try:
                items = request.data.get('items', [])
                if items is None:
                    return Response({'success': False, 'error': 'No items ordered'},
                                    status=status.HTTP_400_BAD_REQUEST)
                
                order_group_id = uuid.uuid4()     

                orders = []
                for item in items:
                    print(order_group_id)
                    print(item)
                    try:
                        laundry_item = Laundry.get_laundry_by_id(id=item['id'])
                        if not current_user.address or not current_user.phone_number:
                            raise ValueError('User address or phone number is missing')
                        order = Order.objects.create(
                            user = current_user,
                            order_group = order_group_id,
                            laundry = laundry_item,
                            quantity = item.get('quantity'),
                            cost = laundry_item.price * item.get('quantity'),
                            address= current_user.address,
                            phone= current_user.phone_number,
                            date = timezone.now()
                        )
                        orders.append(order)
                    except Exception as e:
                        return Response({'success': False, 'error': f'Error processing item {item["id"]}: {e}'},
                                        status=status.HTTP_400_BAD_REQUEST)
                serializer = OrderSerializer(orders, many=True)
                return Response({'success': True, 'orders': serializer.data},
                                    status = status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'success': False, 'error': str(e)},
                                status=status.HTTP_400_BAD_REQUEST)