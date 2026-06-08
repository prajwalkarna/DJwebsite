from django.shortcuts import redirect


class AuthMiddleware:
    PROTECTED_URLS = ["/dashboard/"]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if any(request.path.startswith(url) for url in self.PROTECTED_URLS):
            if not request.user.is_authenticated:
                return redirect("/accounts/login/?next=" + request.path)

        response = self.get_response(request)
        return response
