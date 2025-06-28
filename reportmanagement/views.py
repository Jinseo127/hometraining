import matplotlib
matplotlib.use('Agg')  # GUI 백엔드 대신 Agg 백엔드를 사용

import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from django.shortcuts import render
from .models import Exercise

def generate_graph(exercise):
    fig, ax = plt.subplots(figsize=(5, 3))  # 그래프 크기를 조정 (너비 5, 높이 3)
    attempts = exercise.attempts
    scores = np.linspace(10, 100, attempts)
    ax.bar(range(1, attempts + 1), scores)
    ax.set_xlabel('Attemps')
    ax.set_ylabel('Scores')
    plt.tight_layout()  # 그래프 레이아웃 조정
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graph = base64.b64encode(image_png).decode('utf-8')
    return graph

def report_view(request):
    exercises = Exercise.objects.all()
    exercise_graphs = {exercise.id: generate_graph(exercise) for exercise in exercises}
    context = {
        'exercises': exercises,
        'exercise_graphs': exercise_graphs
    }
    return render(request, 'reportmanagement/report.html', context)
