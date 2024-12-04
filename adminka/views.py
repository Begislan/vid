from django.shortcuts import render, redirect, get_object_or_404
from front.models import *
from .forms import VideoForm, UserForm, TypeForm
from django.contrib.auth.decorators import login_required



@login_required
def adminka_view(request):

    videosList = Video.objects.all()
    context = {
        "videosList": videosList
    }
    return render(request, 'adminka/adminka_list.html', context)
@login_required
def video_create(request):
    form = VideoForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("video_detail", id=form.instance.pk)

    return render(request, 'adminka/create/video_create.html', {'form': form})
@login_required
def video_detail(request, id):
    video = Video.objects.get(id=id)
    return render(request, 'adminka/detail/video_detail.html', {'video': video})

@login_required
def video_update(request, id):
    video = Video.objects.get(id=id)

    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            img = request.FILES.get('img')
            if img is not None:
                video.img = img;
            form.save()
            return redirect('video_detail', id)
    else:
        form = VideoForm(instance=video)

    return render(request, 'adminka/update/video_update.html', {'form': form})

@login_required
def video_delete(request, id):
    video = Video.objects.get(id=id)
    if request.method == 'POST':
        video.delete()
        return redirect('adminka')
    return render(request, 'adminka/delete/video_delete.html', {'video': video})
@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'adminka/user_list.html', {'users': users})
@login_required
def user_detail(request, id):
    user = User.objects.get(id=id)
    return render(request, 'adminka/detail/user_detail.html', {'user': user})
@login_required
def user_create(request):
    form = UserForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('user_admin_detail', id=form.instance.pk)
    return render(request, 'adminka/create/user_create.html', {'form': form})
@login_required
def user_update(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            img = request.FILES.get('img')
            if img is not None:
                user.img = img
            form.save()
            return redirect('user_admin_detail', id)
    else:
        form = UserForm(instance=user)

    return render(request, 'adminka/update/user_update.html', {'form': form})
@login_required
def user_delete(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'adminka/delete/user_delete.html', {'video': user})
@login_required
def feedback_list(request):
    feedback_list = Feedback.objects.all()
    context = {"feedback": feedback_list}
    return render(request, 'adminka/feedback_list.html', context)
@login_required
def cat_list(request):
    cat = Type.objects.all()
    context = {"cat": cat}
    return render(request, 'adminka/cat_list.html', context)

@login_required
def cat_detail(request, id):
    cat = Type.objects.get(id=id)
    context = {"cat": cat}
    return render(request, 'adminka/detail/cat_detail.html', context)
@login_required
def cat_update(request, id):
    cat = get_object_or_404(Type, id=id)

    if request.method == "POST":
        form = TypeForm(request.POST, request.FILES, instance=cat)
        if form.is_valid():
            form.save()
            return redirect('cat_detail', id=cat.id)  # После обновления перенаправляем
    else:
        form = TypeForm(instance=cat)

    context = {"form": form, "cat": cat}
    return render(request, 'adminka/update/cat_update.html', context)


@login_required
def cat_delete(request, id):
    cat = get_object_or_404(Type, id=id)

    if request.method == "POST":
        cat.delete()
        return redirect('cat_list')  # Замените `cat_list` на имя URL, куда перенаправлять после удаления

    context = {"cat": cat}
    return render(request, 'adminka/delete/cat_delete.html', context)


@login_required
def cat_create(request):
    if request.method == "POST":
        form = TypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cat_list')  # Замените `cat_list` на имя URL для списка категорий
    else:
        form = TypeForm()

    context = {"form": form}
    return render(request, 'adminka/create/cat_create.html', context)