from django.shortcuts import render

# Create your views here.
# import random
import random
 
def rand(request,numbers):

    return random.choice(numbers)
    