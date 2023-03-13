from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

from core.apps.authentication.models import User
from core.apps.authentication.serializers import UserCreateSerializer, UserReadSerializer
from core.common.viewsets import CreateListRetrieveViewSet


class UserViewSet(CreateListRetrieveViewSet):
    queryset = User.objects.order_by('-id')
    create_serializer_class = UserCreateSerializer
    read_serializer_class = UserReadSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return self.create_serializer_class
        if self.action in ['list', 'retrieve']:
            return self.read_serializer_class
        return self.serializer_class

    @action(detail=False, serializer_class=UserReadSerializer)
    def me(self, request):
        instance = get_object_or_404(User, pk=request.user.id)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
