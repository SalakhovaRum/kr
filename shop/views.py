
from django.http import HttpResponseRedirect
from .models import CalcHistory


def create(request):
    if request.method == "POST":
        history = CalcHistory()
        history_val1= request.POST.get("20")
        history_val2 = request.POST.get("20")
        history_operator = request.POST.get("результат")
        history.save()
        history_val1.save()
        history_val2.save()
        history_operator.save()
    return HttpResponseRedirect("/")