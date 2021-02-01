import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@csrf_exempt
@require_POST
def test(request):
    json_data = request.body
    data = json.loads(json_data)
    print(json.dumps(data, indent=2))

    return HttpResponse(status=200)
