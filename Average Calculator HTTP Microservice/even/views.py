from django.shortcuts import render

# Create your views here.
def even(numbers):
    count  = 0 
    for num in numbers:
        if num<=10:
            count += 1

    return count
    