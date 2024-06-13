from django.http import HttpResponse
from .models import Message


# Create your views here.

def homePageView(request):
	content = 'Hello Web!';
	id = request.GET.get('id')
	message = Message.objects.get(id=id)
	content = message.content
		
	return HttpResponse(content)
