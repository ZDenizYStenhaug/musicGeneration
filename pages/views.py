from django.shortcuts import render
import src.runner as runner

# Create your views here.
def home_view(request):
    context = {
        "notes": runner.main()
    }
    return render(request, 'home-page.html', context)
