from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from core.models import Order, Laundry
from .serializers import OrderSerializer
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt, csrf_protect
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,logout


@ensure_csrf_cookie
@csrf_protect
@api_view(['POST'])
def user_login_token(request):
    if request.method == 'POST':
        email = request.data.get('Email')
        password = request.data.get('Password')
        user =  authenticate(username=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@ensure_csrf_cookie
def user_logout_token(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            logout(request)
            return Response({'message': 'successfully logged out'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@ensure_csrf_cookie
@permission_classes([IsAuthenticated])
def create_pickup_order(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                items = request.data.get('items', [])
                if items is None:
                    return Response({'success': False, 'error': 'No items ordered'},
                                    status=status.HTTP_400_BAD_REQUEST)
                orders = []
                print(items)
                for item in items:
                    try:
                        laundry_item = Laundry.get_laundry_by_id(id=item['id'])
                        order = Order.objects.create(
                            user = request.user,
                            laundry = laundry_item,
                            quantity = item.get('quantity'),
                            cost = laundry_item.price * item.get('quantity')
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