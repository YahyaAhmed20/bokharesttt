from django.shortcuts import render,redirect
from .forms import ReservationForm

# Create your views here.



def home(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:thank_you')  # ممكن تخليه صفحة شكر مثلاً
    else:
        form = ReservationForm()
    return render(request, 'home/home.html', {'form': form})



def thank_you(request):
    return render(request, 'home/success.html')