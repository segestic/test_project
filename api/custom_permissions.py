from rest_framework.permissions import BasePermission


class IsCustomer(BasePermission):
   def has_permission(self, request, view):
      return request.user.user_type == 1



from rest_framework import permissions #to import SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
	def has_object_permission(self, request, view, obj): # Read-only permissions are allowed for any request
		if request.method in permissions.SAFE_METHODS:
			return True
		# Write permissions are only allowed to the author of a post
		return obj.author == request.user     