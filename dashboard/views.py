from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard_view(request):
    user = request.user
    return render(request, "dashboard/dashboard.html", {"user": user})
