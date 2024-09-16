from django.shortcuts import render # type: ignore

# Create your views here.
def temp1(request):
    d={'name':'Vasavi', 'age':23}
    return render(request, 'temp1.html', context=d)


def temp2(request):
    d={'mobile':[22324356,543665767]}
    return render(request, 'temp1.html', context=d)
