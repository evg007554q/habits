from rest_framework.permissions import BasePermission
from users.models import UserRoles


class IsOwner(BasePermission):
    """Доступ есть у пользователя создателя"""
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
