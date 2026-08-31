from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
  
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def career(request):
    return render(request,'career.html')

def contect(request):

    

    if request.method == 'POST':

        name = request.POST.get('Name', '').strip()
        phone = request.POST.get('Phone', '').strip()
        email = request.POST.get('Email', '').strip()
        company = request.POST.get('Company', '').strip()
        product = request.POST.get('Product', '').strip()
        requirement = request.POST.get('Requirement', '').strip()

        # Validation
        if not name:
            messages.error(request, 'Name is required.')
            return render(request, 'contact.html', {'pro': pro})

        if len(name) < 2:
            messages.error(
                request,
                'Name must be at least 2 characters.'
            )
            return render(request, 'contact.html', {'pro': pro})

        if not phone:
            messages.error(
                request,
                'Phone number is required.'
            )
            return render(request, 'contact.html', {'pro': pro})

        if not phone.isdigit():
            messages.error(
                request,
                'Phone number must contain only digits.'
            )
            return render(request, 'contact.html', {'pro': pro})

        if len(phone) != 10:
            messages.error(
                request,
                'Phone number must be 10 digits.'
            )
            return render(request, 'contact.html', {'pro': pro})

        if email:
            try:
                validate_email(email)
            except ValidationError:
                messages.error(
                    request,
                    'Please enter a valid email address.'
                )
                return render(
                    request,
                    'contact.html',
                    {'pro': pro}
                )

        if not product:
            messages.error(
                request,
                'Please select a product.'
            )
            return render(
                request,
                'contact.html',
                {'pro': pro}
            )

        # Save enquiry
        # Enquiry.objects.create(
        #     name=name,
        #     phone=phone,
        #     email=email or None,
        #     company=company or None,
        #     product=product,
        #     requirement=requirement or None
        # )

        # Send email
        subject = f'New Enquiry - {name}'

        message = f"""
New Enquiry Received

Name: {name}
Phone: {phone}
Email: {email}
Company: {company}
Product / Service: {product}

Requirement:
{requirement}
"""
        try: 
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['kpsales32@gmail.com'],
                fail_silently=False,
            )

            messages.success(
                request,
                'Your enquiry has been submitted successfully.'
            )
        except exceptions as e:
              print('error',e)
        return redirect('contact')
    return render(
            request,
            'contact.html',
        
        )
    # return render(
    #     request,
    #     'contact.html',
    #     {'pro': pro}
    # )

def allproduct(request):
    pro=ProductCategory.objects.all()
    
    return render(request,'products.html',{"pro":pro})

def product(request):
    pro=Product.objects.filter(is_active=True)
    return render(request,'admixtures.html',{"pro":pro})