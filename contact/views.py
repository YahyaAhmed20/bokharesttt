from django.shortcuts import render,redirect
from django.contrib import messages
from .models import ContactMessage
# Create your views here.


def send_text(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # حفظ الرسالة في قاعدة البيانات
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, "تم إرسال رسالتك بنجاح وتم حفظها في قاعدة البيانات ✅")
        return redirect('contact:success')
    return render(request,'contact/contact.html')



def success(request):
    return render(request, 'contact/success.html')

