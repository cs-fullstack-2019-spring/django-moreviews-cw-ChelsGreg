from django.shortcuts import render
from django.http import HttpResponse
from .models import Cup

# Create your views here.
#
# TEST FUNCTION
def index(request):
    return HttpResponse("Test URL")

# FUNCTION FOR HELLO, NAME
def helloThere(request, name):
    return HttpResponse("Hello, " + name + "!")

# FUNCTION FOR NUMBER TIMES 2
def timesTwo(request, number):
    return HttpResponse("Your number times 2 is: " + str(number*2))

# FUNCTION TO ADD NUMBERS TO SUM
def sumofAll(request, number):
    sum = 0
    for nums in range (0, number):
        sum += number
        return HttpResponse(nums)


# FUNCTION TO CREATE NEW CUP OBJECT
def createCup(request):
    viewAll= Cup.objects.all()
    newCup = Cup.objects.create(name="Wine", material="Glass", manufactuerDate='2016-01-10')
    newCup2 = Cup(name="Shots", material="Plastic", manufactuerDate='2017-03-12')
    newCup2.save()
    return HttpResponse(viewAll)

# FILTERS FOR MANUFACTURE DATE
def allCups(request):
    onlyDate = Cup.objects.filter('manufactuerDate')
    return HttpResponse(onlyDate)

# CHANGE MATERIAL THROUGH MANUFACTURE DATE
def changeMat(request):
    onlyDate= Cup.objects.filter(manufactuerDate__gt = '2012-01-01')
    for eachCup in onlyDate:
        Cup.object.material = "slightly new"

    return HttpResponse(onlyDate)

# FUNCTION FOR CUP INDEX TO PRINT
def cupIndex(request):
    viewAll = Cup.objects.all()
    after2012 = Cup.objects.filter(manufactuerDate__gt='2012-12-31')
    context = {
        "viewAll": viewAll,
        "after2012": after2012,
    }

    return render(request, "cupApp/index.html", context)



