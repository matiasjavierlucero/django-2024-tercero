from users.models import Profile

def profile(request):
    if not request.user.is_anonymous:
        profile = Profile.objects.get(user=request.user)
    else:
        profile=None
    return dict(
        profile=profile
    )