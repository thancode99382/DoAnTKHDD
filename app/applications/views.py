from django.shortcuts import render, redirect
from django.utils.text import slugify

from users.forms import RecruitmentForm


# Create your views here.
def post_recruitment(request):
    if request.method == 'POST':
        form = RecruitmentForm(request.POST, user=request.user)
        if form.is_valid():
            recruitment = form.save(commit=False)
            recruitment.slug = slugify(recruitment.title)
            recruitment.save()
            return redirect('core:home')
    else:
        form = RecruitmentForm(user=request.user)
    return render(request, 'applications/post_recruitment.html', {'form': form})
