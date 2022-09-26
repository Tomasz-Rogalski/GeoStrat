from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
  def wrapper_func(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('blogapp:home')
    else:
      return view_func(request, *args, **kwargs)

  return wrapper_func

def allowed_users(allowed = []):
  def decorator(view_func):
    def wrapper_func(request, *args, **kwargs):
      group = None
      if request.user.groups.exists():
        group = request.user.groups.all()
        if any(g.name in allowed for g in group):
          return view_func(request, *args, **kwargs)
        else:
          return HttpResponse('u are not autorized')
    return wrapper_func
  return decorator
