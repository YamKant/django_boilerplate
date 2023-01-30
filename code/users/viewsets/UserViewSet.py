from rest_framework import viewsets
from users.models import DjangoUser, User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet): 
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = User.objects.all()
    # serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


