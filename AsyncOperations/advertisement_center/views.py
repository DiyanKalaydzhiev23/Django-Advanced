from django.contrib import messages
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from advertisement_center.forms import CommercialForm
from advertisement_center.models import Commercial
from advertisement_center.tasks import enqueue_video_processing
from advertisement_center.utils import stats_counts, get_queue_sizes


def index(request):
    context = {
        'commercials': Commercial.objects.all(),
        'auto_refresh_ms': 4000,
        **stats_counts(),
    }
    return render(request, 'advertisement_center/commercial_list.html', context)

def create_commercial(request):
    form = CommercialForm(request.POST or None, request.FILES or None)

    context = {'form': form}

    if request.method == "POST":
        commercial = form.save()
        transaction.on_commit(lambda: enqueue_video_processing(commercial.pk, 'heavy'))
        messages.success(request, message='Commercial saved and send to heavy queue')
        return redirect('advertisement_center:index')

    return render(request, 'advertisement_center/commercial_form.html', context)

def refresh_slogan(request, pk):
    if request.method == "POST":
        commercial = get_object_or_404(Commercial, pk=pk)
        try:
            enqueue_video_processing(commercial.pk, 'light')
            messages.info(request, 'Slogan refresh queued on light queue')
        except Exception as exc:
            messages.error(request, f"Unable to update slogan {exc}")

    return redirect('advertisement_center:index')


def task_monitor(request):
    context = {'queue_sizes': get_queue_sizes(), **stats_counts()}
    print(context['queue_sizes'])
    return render(request, 'advertisement_center/task_monitor.html', context)