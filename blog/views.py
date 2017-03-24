from django.shortcuts import render

# Create your views here.
def blog_list(request):
    return render(request, 'admin/home.html', {})

def account(request):
    return render(request, 'admin/account.html', {})
