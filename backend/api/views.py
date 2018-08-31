

from django.http import HttpResponse, HttpRequest, JsonResponse
from . import repositories
from . import tags

sentence_repo = repositories.SentenceRepository()

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello. This is the api index")

def sentences(request: HttpRequest) -> HttpResponse:
    count = int(request.GET.get('count', 10))

    _sentences = sentence_repo.get(count)
    response = {'status': 200, 'sentence_count': count}
    response['sentences'] = _sentences

    _tags = tags.get()
    response['tag_count'] = len(_tags)
    response['tags'] = _tags

    return JsonResponse(response)

def sentence_tags(request: HttpRequest) -> HttpResponse:

    return JsonResponse({'status': 200, 'successful': True})



