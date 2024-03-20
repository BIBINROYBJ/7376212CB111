from django.shortcuts import render

# Create your views here.
def fibo(numbers):
    
    for n in numbers:
        if(n<=10):
            if n < 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            elif n == 0:
                return 0

            else:
                return fibo(n-1) + fibo(n-2)


