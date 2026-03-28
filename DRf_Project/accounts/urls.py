from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls



# | Method | URL             | Action      |
# | ------ | --------------- | ----------- |
# | POST   | `/api/users/`   | Create user |
# | GET    | `/api/users/`   | List users  |
# | GET    | `/api/users/1/` | Retrieve    |
# | PUT    | `/api/users/1/` | Update      |
# | DELETE | `/api/users/1/` | Delete      |
