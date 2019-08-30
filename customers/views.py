from django.shortcuts import render, render_to_response
from customers.models import Customers, ContracOfNumber
from django.template.context_processors import csrf

def main(request):
    return render_to_response('main.html')


def client_created_form(request):
    arqs = {}
    arqs.update(csrf(request))
    return render_to_response('client_created_form.html', arqs)


def form_f(request):
    arqs = {}
    arqs.update(csrf(request))
    return render_to_response('form_f.html', arqs)


def form_u(request):
    arqs = {}
    arqs.update(csrf(request))
    return render_to_response('form_u.html', arqs)

def fop_create(request):
    arqs = {}
    arqs.update(csrf(request))
    if request.POST:
        client_code = request.POST.get('client_code', '')
        first_name = request.POST.get('first_name', '')
        second_name = request.POST.get('second_name', '')
        patronymic = request.POST.get('patronymic', '')
        value_added_tax = request.POST.get('value_added_tax', '')
        extract = request.POST.get('extract', '')
        passport = request.POST.get('passport', '')
        single_tax = request.POST.get('single_tax', '')
        general_tax = request.POST.get('general_tax', '')
        notes = request.POST.get('notes', '')
        if value_added_tax == '':
            value_added_tax = None
        if extract == 'on':
            extract = True
        else:
            extract = False
        if passport == 'on':
            passport = True
        else:
            passport = False
        if single_tax == 'on':
            single_tax = True
        else:
            single_tax = False
        if general_tax == 'on':
            general_tax = True
        else:
            general_tax = False
        cn = ContracOfNumber.objects.all()
        x=0
        for i in cn:
            x+=1
        cn =  ContracOfNumber(contrac_of_number=x+1)
        cn.save()

        # try:
        #     print("try")
        #     contract_number = ContracOfNumber.objects.all()
        #     x = 0
        #     for i in contract_number:
        #         x=+1
        #     cn = contract_number[x].contrac_of_number+1
        #     contract_number = ContracOfNumber(contrac_of_number=cn)
        #     contract_number.save()
        # except:
        #     print("except")
        #     contract_number = ContracOfNumber(contrac_of_number=1)
        #     contract_number.save()
        #     cn = 1
        fop = Customers(client_code=client_code, first_name=first_name,
                        second_name=second_name, patronymic=patronymic,
                        value_added_tax=value_added_tax, extract=extract,
                        passport=passport, single_tax=single_tax,
                        general_tax=general_tax, notes=notes, contract_number = x+1)
        fop.save()
    return render_to_response('client_created_form.html', arqs)


def legal_person_create(request):
    arqs = {}
    arqs.update(csrf(request))
    return render_to_response('client_created_form.html', arqs)