from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults




def predict(request):
    sepal_length = 0
    sepal_width = 0
    petal_length = 0
    petal_width = 0
    classification = "None"
    if request.method == 'POST':

        # Receive data from client
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        # Unpickle model
        model = pd.read_pickle(r"C:\Users\AL MASRIA 4 COMP\Desktop\iris\new_model.pickle")
        # Make prediction
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        classification = result[0]

        PredResults.objects.create(sepal_length=sepal_length, sepal_width=sepal_width, petal_length=petal_length,
                                   petal_width=petal_width, classification=classification)

    context = {
    'sepal_length': sepal_length,
    'sepal_width':sepal_width,
    'petal_length': petal_length,
    'petal_width':petal_width,
    'classification': classification
    }
    return render(request, 'predict.html', context)


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)
