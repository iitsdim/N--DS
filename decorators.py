from functools import wraps


def permit_if_role_in(allowed_roles=()):
    def _(f):
        @wraps(f)
        def user_permissions(view, request, *args, **kwargs):
            print(allowed_roles, request.role)
            if getattr(request, 'role', False) not in allowed_roles:
                return -1

            response = f(view, request, *args, **kwargs)
            return response

        return user_permissions

    return _


class Request:
    pass


request = Request()
setattr(request, 'role', 'USER')


class VIEW:
    @permit_if_role_in(['USER'])
    def get(self, request):
        return 1


my_view = VIEW()

print(my_view.get(request))
