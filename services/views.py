from django.shortcuts import render

# Create your views here.
def service_view(request):
    return render(request,'services.html')

def service_detail(request):
    return render(request,'service_detail.html')