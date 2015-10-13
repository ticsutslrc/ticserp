from django.shortcuts import render

# Create your views here.
def main(request):
    """
    Vista principal
    """
    return render(request, 'planeacion/index.html')
