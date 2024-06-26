from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import File


@login_required
def deleteView(request):
	f = File.objects.get(pk=request.POST.get('id'))
	if request.user.username != f.owner.username:
		return redirect('/')
	f.delete()
	return redirect('/')
	

@login_required
def downloadView(request, fileid):
	f = File.objects.get(pk=fileid)
	if request.user.username != f.owner.username:
		return redirect('/')
	filename = f.data.name.split('/')[-1]
	response = HttpResponse(f.data, content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename=%s' % filename

	return response


@login_required
def addView(request):
	data = request.FILES.get('file')
	f = File(owner=request.user, data=data)
	f.save()
	return redirect('/')


@login_required
def homePageView(request):
	files = File.objects.filter(owner=request.user)
	uploads = [{'id': f.id, 'name': f.data.name.split('/')[-1]} for f in files]	
	return render(request, 'pages/index.html', {'uploads': uploads})
