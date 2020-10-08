from rest_framework import permissions



class IsAdminOrIsTeacher(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff and request.user.is_teacher)


