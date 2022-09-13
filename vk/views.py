import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from vk.models import VkUser
from vk.serializers import convert_vk_user_to_dict
from vk.services import VKService


def index(request):
    data = VkUser.objects
    return render(request, 'vk/index.html', {'items': data})


def vk_authorization(request):
    return redirect("https://oauth.vk.com/authorize?client_id=51425431&display=page&redirect_uri=http://localhost"
                    ":8000/callback&response_type=token&revoke=1&scope=")


def vk_callback(request):
    if len(request.GET) == 0:
        return render(request, 'vk/callback.html')
    access_token = request.GET.get('access_token', '')
    if access_token == '':
        return redirect('/')

    service = VKService()
    _ = service.get_users(access_token)
    return redirect('/')


def json_file_data(request):
    data = [convert_vk_user_to_dict(user) for user in VkUser.objects.all()]
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename=export.json'
    return response


def json_data(request):
    data = [convert_vk_user_to_dict(user) for user in VkUser.objects.all()]
    return JsonResponse(data, safe=False)
