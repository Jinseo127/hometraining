from django.shortcuts import render

def video(request):
    return render(request, 'videomanagement/video.html')
