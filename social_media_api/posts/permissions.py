from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only the author can edit or delete their own post/comment.
    Others can only view (read-only access).
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS → always allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Otherwise, only allow if the user is the author
        return obj.author == request.user
