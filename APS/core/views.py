from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
from .API.HGFinanceConnection import taxes, quotations, bovespa

# Create your views here.

parametroEmpresa = ''

@csrf_protect
def empresaCode(request):
    if request.POST:

        global parametroEmpresa
        empresa = request.POST.get('empresa')
        parametroEmpresa = empresa

    print(parametroEmpresa)

    return redirect('http://localhost:8000/')

class main_finance(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, *args, **kwargs):

        global parametroEmpresa
        if parametroEmpresa != '':
            context = {
                'taxes' : taxes(),
                'quotationsUSD': quotations('USD'),
                'quotationsEUR': quotations('EUR'),
                'quotationsGBP': quotations('GBP'),
                'quotationsARS': quotations('ARS'),
                'quotationsBTC': quotations('BTC'),
                'acoes': bovespa(parametroEmpresa),
            }
        else:
            context = {
                'taxes': taxes(),
                'quotationsUSD': quotations('USD'),
                'quotationsEUR': quotations('EUR'),
                'quotationsGBP': quotations('GBP'),
                'quotationsARS': quotations('ARS'),
                'quotationsBTC': quotations('BTC'),
                'acoes': bovespa('PETR4'),
            }

        return context

'''
def main_finance(request):

    return render(request, 'main.html')
    
    if empresaCodigo != '':
        jsonEmpresa = bovespa(empresaCodigo),    
    
'''


