from django.shortcuts import render

def bad_request(request, exception):
    return render(request, "errors/400.html")

def permission_denied(request, exception):
    return render(request, "errors/403.html")

def page_not_found(request, exception):
    return render(request, "errors/404.html")

def server_error(request, exception=None):
    return render(request, "errors/500.html")

