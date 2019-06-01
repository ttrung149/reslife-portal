from residencies.models import Resident


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter_resident(request):
    residents = Resident.objects.all()

    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    student_ID = request.GET.get('student_ID')
    room_number = request.GET.get('room_number')
    building = request.GET.get('building')
    under_RA = request.GET.get('under_RA')

    if is_valid_queryparam(first_name):
        residents = residents.filter(first_name=first_name)

    elif is_valid_queryparam(last_name):
        residents = residents.filter(last_name=last_name)

    elif is_valid_queryparam(student_ID):
        residents = residents.filter(student_ID=student_ID)

    elif is_valid_queryparam(room_number):
        residents = residents.filter(room__room_number=room_number)

    elif is_valid_queryparam(building):
        residents = residents.filter(room__building__id=building)

    elif is_valid_queryparam(under_RA):
        residents = residents.filter(under_RA__user__id=under_RA)
    return residents
