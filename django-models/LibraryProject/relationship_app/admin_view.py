from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .views import check_role

@login_required
@user_passes_test(lambda user: check_role(user, 'Admin'), login_url='/login/')
def admin_view(request):
    return render(request, 'admin_view.html', {'role': 'Admin'})
