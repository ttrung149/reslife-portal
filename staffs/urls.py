from django.urls import path
from . import views
from staffs import views

from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('', login_required(IRListView.as_view()), name='home'),
    # path('about/', views.about, name='blog-about'),
    # path('ir/<int:pk>/', login_required(IRDetailView.as_view()), name='ir-detail'),
    # path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    # path('ir/new/', login_required(IRCreateView.as_view()), name='ir-create'),
    path('profile/update', login_required(views.update_profile),
         name='update-profile'),
    path('profile/', login_required(views.profile), name='profile'),
]
