from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .views import check_role

@login_required
@user_passes_test(lambda user: check_role(user, 'Member'), login_url='/login/')
def member_view(request):
    return render(request, 'member_view.html', {'role': 'Member'})
