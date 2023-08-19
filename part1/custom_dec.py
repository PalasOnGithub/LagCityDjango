from django.core.exceptions import PermissionDenied
from functools import wraps
from .models import Plant
from django.shortcuts import redirect



def require_common_user(view):
	@wraps(view)
	def _view(request, *args, **kwargs):
		try:
			if Plant.objects.filter(from_user=request.user).first():
				return redirect('/music/')
		except:
			pass
		return view(request, *args, **kwargs)
	return _view
