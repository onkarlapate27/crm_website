from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..models.customer_model import Customer
from django.contrib import messages

def list_customers(request):
    try:
        all_customers_data = Customer.objects.all()
        return render(request=request, template_name='customers.html', context={"all_customers_data": all_customers_data})

    except Exception as e:
        print("Unable to list customers.", e)
        return HttpResponse("Error processing list customers request.", status=500)

def add_customer(request):
    try:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            city = request.POST.get('city')
            pincode = request.POST.get('pincode')
            country = request.POST.get('country')

            customer = Customer()
            customer.first_name = first_name
            customer.last_name = last_name
            customer.phone = phone
            customer.address = address
            customer.city = city
            customer.pincode = pincode
            customer.country = country
            customer.save()

            messages.success(request, 'Customer data added successfully.')
            return redirect('customers')

        else:
            return render(request, 'add_customer.html')

    except Exception as e:
        print("Unable to add customer.", e)
        return HttpResponse("Error processing add customer request.", status=500)
    
def update_customer(request, customer_id):
    try:
        customer_data = Customer.objects.get(id = customer_id)
        if not customer_data:
            messages.success(request, 'Customer does not exists.')
            return redirect('customers')

        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            city = request.POST.get('city')
            pincode = request.POST.get('pincode')
            country = request.POST.get('country')

            customer_data.first_name = first_name
            customer_data.last_name = last_name
            customer_data.phone = phone
            customer_data.address = address
            customer_data.city = city
            customer_data.pincode = pincode
            customer_data.country = country
            customer_data.save()

            messages.success(request, 'Customer data updated successfully.')
            return redirect('customers')

        else:
            return render(request, 'update_customer.html', context={"customer_details": customer_data})

    except Exception as e:
        print("Unable to update customer.", e)
        return HttpResponse("Error processing update customer request.", status=500)
    
def delete_customer(request, customer_id):
    try:
        customer_data = Customer.objects.get(id = customer_id)
        if not customer_data:
            messages.success(request, 'Customer does not exists.')
            return redirect('customers')
        
        customer_data.delete()

        return redirect('customers')

    except Exception as e:
        print("Unable to delete customers.", e)
        return HttpResponse("Error processing delete customer request.", status=500)