from json import dumps


from django.http import HttpResponse
from django.db.models import Q

from contact.models import contact

# getting total list
def getList(request):
    return HttpResponse(dumps([i.toJson for i in contact.objects.get_queryset()]))



# adding new person
def  addPerson(request):
    errors = ''

    if (request.POST.get('name') is None):
        errors += "name is not in post request\n"

    if (request.POST.get('family') is None):
        errors += "family is not in post request\n"

    if (request.POST.get('number') is None):
        errors += "number is not in post request\n"

    if errors:
        return HttpResponse(errors)

    if (contact.objects.filter(Q(name=request.POST['name']) | Q(family=request.POST['family']) |
                                   Q(number=request.POST['number'])).exists()):
        return HttpResponse("there is a person with this attributes")

    contact(name=request.POST['name'], family=request.POST['family'], number=request.POST['number']).save()
    return HttpResponse("New person added")



def delPerson(request):
    removed = {}

    if (request.POST.get('name') is not None):
        removed['name'] = contact.objects.filter(name=request.POST.get('name')).delete()

    if (request.POST.get('family') is not None):
        removed['family'] = contact.objects.filter(family=request.POST.get('family')).delete()

    if (request.POST.get('phone') is not None):
        removed['phone'] = contact.objects.filter(phone=request.POST.get('phone')).delete()

    return HttpResponse(dumps(removed))



# updating contact info by id
def update(request):
    if (request.POST.get('id') is None):
        return HttpResponse("Id is not in request")

    ct = contact.objects.filter(id=request.POST.get('id'))[:1]
    if ct.count() == 0:
        return HttpResponse("There is no person with this Id")
    ct = ct[0]

    if (request.POST.get('name') is not None):
        ct.name = request.POST.get('name')

    if (request.POST.get('family') is not None):
        ct.family = request.POST.get('family')

    if (request.POST.get('phone') is not None):
        ct.phone = request.POST.get('phone')

    ct.save()
    return HttpResponse(dumps(ct.toJson()))

