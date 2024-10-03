from users.models import Profile

def profile(request):
    return dict(
        profile=Profile.objects.get(user=request.user)
    )