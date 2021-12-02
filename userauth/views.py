
from django.shortcuts import render

# Create your views here.

from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView

# Create your views here.
@login_required
def profile_view(request):
    return render(request, 'account/profile.html')