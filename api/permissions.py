from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
	def has_object_permession(self, request, obj):
		if request.user.is_staff:
			return True 
		else:
			return False	