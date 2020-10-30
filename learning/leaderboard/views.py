from django.shortcuts import render
from discussions.models import Reward
# Create your views here.

def leaderHome(request):
    users = Reward.objects.all()
    curuser = Reward.objects.filter(user=request.user).first()
    context = {'users' : users, 'curuser': curuser}
    return render(request, 'leaderboard_home.html', context)