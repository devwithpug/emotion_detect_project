from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FaceView

face_list = FaceView.as_view({
    'post': 'create',
    'get': 'list',
})

face_detail = FaceView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework!')),
    path('face/', face_list, name='post_list'),
    path('face/<int:pk>/', face_detail, name='post_detail')
])