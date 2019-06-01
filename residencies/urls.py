from django.urls import path
from . import views

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('room-inspection/', login_required(views.roomInspectionView),
         name='room-inspection'),
    path('inspect/room/<int:pk>',
         login_required(views.inspectRoomView), name='inspect-room'),
    path('checkout/', login_required(views.checkoutView), name='checkout'),
    path('checkout/resident/<int:pk>',
         login_required(views.checkoutResidentView), name='checkout-resident')
]
