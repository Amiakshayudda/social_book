from django.shortcuts import render, redirect
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from users.models import UploadBooks

# Create your views here.

@login_required(login_url='../account/login.html')
def fetchall(request):
    allusers = CustomUser.objects.filter(public_visibility=True)
    return render(request, 'fetchall.html', {'allusers': allusers})

@login_required(login_url='../account/login.html')
def uploadbooks(request):
    if request.method == 'POST':
        title = request.POST['title']
        cost = int(request.POST['cost'])
        year_of_publishing = int(request.POST['year_of_publishing'])
        description = request.POST['description']
        cover_image = request.FILES['cover_image']
        book_path = request.FILES['book_path']
        visibility = bool(request.POST.get('visibility', False))

        uploadbooks = UploadBooks.objects.create(CustomUser=request.user, title=title, cost=cost, year_of_publishing=year_of_publishing, description=description, cover_image=cover_image, book_path=book_path, visibility=visibility)
        uploadbooks.save()
        return redirect('uploadbooks')
    else:
        return render(request, 'uploadbooks.html')
    
@login_required(login_url='../account/login.html')
def viewbooks(request):
    uploadedbooks = UploadBooks.objects.filter(CustomUser=request.user)
    return render(request, 'viewbooks.html', {'uploadedbooks': uploadedbooks})