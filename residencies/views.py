from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse
from residencies.models import Resident, Building, Room
from staffs.models import Staff
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import filter_resident


def checkoutView(request):
    num_items_per_page = 15
    filtered_results = filter_resident(request)
    page = request.GET.get('page', 1)
    paginator = Paginator(filtered_results, num_items_per_page)

    try:
        filtered_results = paginator.page(page)
    except PageNotAnInteger:
        filtered_results = paginator.page(1)
    except EmptyPage:
        filtered_results = paginator.page(paginator.num_pages)

    buildings = Building.objects.all()
    staffs = Staff.objects.all()

    context = {
        'filtered_results': filtered_results,
        'buildings': buildings,
        'staffs': staffs
    }
    return render(request, 'residencies/check_out.html', context)


def checkoutResidentView(request, pk):
    if request.method == 'POST' and 'checkout' in request.POST:
        resident = Resident.objects.get(id=pk)
        resident.is_checked_out = True
        resident.checked_out_by = request.user.staff
        resident.checked_out_time = timezone.now()
        resident.save()
        messages.success(request, f'Resident {resident} is checked out!')

    elif request.method == 'POST' and 'undo' in request.POST:
        resident = Resident.objects.get(id=pk)
        resident.is_checked_out = False
        resident.checked_out_by = None
        resident.checked_out_time = None
        resident.save()
        messages.warning(request, f'Resident {resident} is not checked out!')

    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    student_ID = request.POST.get('student_ID')
    room_number = request.POST.get('room_number')
    building = request.POST.get('building')
    under_RA = request.POST.get('under_RA')
    page = request.POST.get('page')

    redirect_URL = f'/checkout/?first_name={first_name}&last_name={last_name}&student_ID={student_ID}&room_number={room_number}&building={building}&under_RA={under_RA}&page={page}'

    return redirect(redirect_URL)


def roomInspectionView(request):
    num_items_per_page = 15

    filtered_results = filter_resident(request)
    page = request.GET.get('page', 1)
    paginator = Paginator(filtered_results, num_items_per_page)

    try:
        filtered_results = paginator.page(page)
    except PageNotAnInteger:
        filtered_results = paginator.page(1)
    except EmptyPage:
        filtered_results = paginator.page(paginator.num_pages)

    buildings = Building.objects.all()
    staffs = Staff.objects.all()
    context = {
        'filtered_results': filtered_results,
        'buildings': buildings,
        'staffs': staffs
    }

    return render(request, 'residencies/room_inspection.html', context)


def inspectRoomView(request, pk):
    if request.method == 'POST' and 'pass_inspection' in request.POST:
        room = Room.objects.get(id=pk)
        room.pass_inspection = True
        room.inspected_by = request.user.staff
        room.inspection_time = timezone.now()
        room.save()
        messages.success(request, f'Room {room} passed inspection!')

    elif request.method == 'POST' and 'fail_inspection' in request.POST:
        room = Room.objects.get(id=pk)
        room.pass_inspection = False
        room.inspected_by = request.user.staff
        room.inspection_time = timezone.now()
        room.save()

        messages.warning(
            request, f'Room {room} is marked failed for inspection!')

    elif request.method == 'POST' and 'undo' in request.POST:
        room = Room.objects.get(id=pk)
        room.pass_inspection = False
        room.inspected_by = None
        room.inspection_time = None
        room.save()

        messages.warning(
            request, f'Room {room} is not inspected!')

    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    student_ID = request.POST.get('student_ID')
    room_number = request.POST.get('room_number')
    building = request.POST.get('building')
    under_RA = request.POST.get('under_RA')
    page = request.POST.get('page')

    redirect_URL = f'/room-inspection/?first_name={first_name}&last_name={last_name}&student_ID={student_ID}&room_number={room_number}&building={building}&under_RA={under_RA}&page={page}'

    return redirect(redirect_URL)
