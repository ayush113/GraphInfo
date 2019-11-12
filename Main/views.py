from django.shortcuts import render
from django.views.decorators import csrf
from Main.AppLogic.main import run
import glob

# Create your views here.
@csrf.csrf_exempt
def main(request):
    try:
        data = request.GET['data-text']
        print(type(data))
        # Run the script here
        run(data)
        img_addresses = glob.glob('static/Main/img/Plots/*.png')
        for i in range(len(img_addresses)):
            img_addresses[i] = img_addresses[i].split('static/')[1]
    except:
        print("NONE")
        img_addresses = None
    return render(request,'Main/index.html',{'imgs':img_addresses })