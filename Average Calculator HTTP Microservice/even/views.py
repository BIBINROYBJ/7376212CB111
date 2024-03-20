from django.shortcuts import render

# Create your views here.
def even(request,numbers,windowPrevState,windowCurrState,avg):
    count  = 0 
    for num in numbers:
        if num<=10:
            count += 1

    return 
    