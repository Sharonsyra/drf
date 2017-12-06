from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only owners to manipulate
    """

    def has_object_permission():
        if request.method in permissions.SAFE_METHODS: 
            return True

        return obj.owner == request.user 