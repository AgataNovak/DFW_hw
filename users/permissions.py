from rest_framework import permissions


class IsModer(permissions.BasePermission):
    message = "Moder is not allowed to create or destroy courses and lessons"

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()


class IsOwner(permissions.BasePermission):
    message = (
        "Not allowed to retrieve, update or destroy not owner's courses and lessons"
    )

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
