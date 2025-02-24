from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .views import check_role

@login_required
@user_passes_test(lambda user: check_role(user, 'Librarian'), login_url='/login/')
def librarian_view(request):
    return render(request, 'librarian_view.html', {'role': 'Librarian'})
