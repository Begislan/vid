from django.shortcuts import render, redirect
from .models import *
from .models import Feedback
from .forms import FeedbackForm
from django.core.paginator import Paginator

# Create your views here.
def front_core(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Сохранение данных в базе данных
            return redirect('feedback_success')  # Перенаправление после успешного отправления
    else:
        form = FeedbackForm()
    typeVideos = Type.objects.all()
    videos = Video.objects.all()[:2]
    context = {
        'typeVideos': typeVideos,
        'videos': videos,
        'form': form
    }
    return render(request, 'front/index.html', context)

def feedback_success(request):
    return render(request, 'front/feedback_success.html')


def full_videos(request):
    videos = Video.objects.all()

    paginator = Paginator(videos, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'front/video.html', locals())


def video_details(request, id):
    video = Video.objects.get(id=id)

    return render(request, 'front/video_detail.html', locals())

def users(request):
    users = User.objects.all()
    paginator = Paginator(users, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'front/users.html', locals())


def user_detail(request, id):
    videos = Video.objects.filter(user__id=id)
    user = videos.all()
    return render(request, 'front/user_detail.html', locals())

def mentor_details(request,pk):
    videos = Video.objects.filter(user__id=pk)
    user = videos.all()
    return render(request, 'app/mentor/mentor.html', {'user': user, "videos": videos})

def category_list(request):
    typeVideos = Type.objects.all()
    return render(request, 'front/category_list.html', locals())

def category_details(request, pk):
    videos = Video.objects.filter(type__id=pk)
    type = videos.all()
    return render(request, 'front/category_detail.html', locals())