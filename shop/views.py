from django.shortcuts import redirect, render

from .models import CalcHistory


def get_receive(symbol, r, s):
    lll = {'*': lambda r, s: r * s,
            '+': lambda r, s: r + s,
            '-': lambda r, s: r - s,
            '/': lambda r, s: r // s
            }
    return lll[symbol](r, s)


def calculate_view(request):
    form = CalcHistory()
    if request.method == 'POST':
        symbol = str(request.POST.get('operator'))
        val1 = int(request.POST.get('val1'))
        val2 = int(request.POST.get('val2'))
        result = get_receive(symbol, val1, val2)
        form = CalcHistory(request.POST, initial={'result': result})
        if form.is_valid():
            form.save()
            return redirect('calculate')

    return render(request, template_name='shop/main.html', context={'form': form})


def conclusion_view(request):
    storage = CalcHistory.objects.all()
    return render(request, "shop/storage.html", context={'storage': storage})
