from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required()
def main(request):
    """
    Vista principal
    """
    return render(request, 'mainapp/index.html')
