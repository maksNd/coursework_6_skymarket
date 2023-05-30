from django.urls import include, path

# TODO настройка роутов для модели
from rest_framework import routers

from ads.views import AdViewSet

from ads.views import CommentViewSet

ads_router = routers.SimpleRouter()
ads_router.register('ads', AdViewSet)

comment_router = routers.SimpleRouter()
comment_router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(ads_router.urls)),

    path('', include(comment_router.urls)),

    path("ads/<int:ad_id>/comments/", CommentViewSet.as_view({"get": "list", "post": 'create'})),
    path("ads/<int:ad_id>/comments/<int:id>/", CommentViewSet.as_view({'get': 'retrieve',
                                                                       'put': 'update',
                                                                       'patch': 'partial_update',
                                                                       'delete': 'destroy'})),
]
