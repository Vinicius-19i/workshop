from django.http import JsonResponse

def teste_view(request):
    return JsonResponse({"Rota":'Teste!'})

def endoidou(request):
    return JsonResponse({"Logo:":"Heitor!"})