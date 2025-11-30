from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import UserName

@csrf_exempt
def save_name(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get("name")
        UserName.objects.create(name=name)
        return JsonResponse({"message": "Name saved successfully"})
    else:
        return JsonResponse({"error": "Invalid request method"})


@csrf_exempt
def list_names(request):
    if request.method == 'GET':
        name = list(UserName.objects.values_list('name', flat=True))
        return JsonResponse({'names': name})
    else:
        return JsonResponse({'error': 'Get request required'},status=400)
    
@csrf_exempt
def delete_name(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        name = data.get("name")

        if not name:
            return JsonResponse({"error": "Name is required"}, status=400)

        deleted = UserName.objects.filter(name=name).delete()

        if deleted[0] == 0:
            return JsonResponse({"error": "Name not found"}, status=404)

        return JsonResponse({"message": "Name deleted successfully"})

    return JsonResponse({"error": "POST request required"}, status=400)