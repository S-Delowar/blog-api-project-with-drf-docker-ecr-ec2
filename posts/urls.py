from django.urls import path

from posts.views import PostDetail, PostList, UserDetail, UserList

urlpatterns = [
    path('', PostList.as_view(), name="post_list"),
    path('<int:pk>/', PostDetail.as_view(), name="post_detail"),
    path('users/', UserList.as_view(), name="users"),
    path('users/<int:pk>/', UserDetail.as_view(), name="user_detail")
]

# from rest_framework.routers import SimpleRouter
# from .views import PostViewSet, UserViewSet

# router = SimpleRouter()
# router.register("users", UserViewSet, basename="users")
# router.register("posts", PostViewSet, basename="posts")

# urlpatterns = router.urls
