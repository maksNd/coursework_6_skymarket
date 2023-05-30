# TODO здесь производится настройка пермишенов для нашего проекта
from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.author:
            return request.user == obj.author
        return False


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role:
            return request.user.role == 'admin'
        return False
