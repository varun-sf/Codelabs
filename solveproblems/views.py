import json
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import ProblemForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def problems_list(request):
    template = loader.get_template('all_problems.html')
    context = {}
    return HttpResponse(template.render(context,request))


def problem_detail(request, problem_id):
    template = loader.get_template('problem_detail.html')
    context = {}
    return HttpResponse(template.render(context,request))



@csrf_exempt
def add_problem(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON data from the request body
        except json.JSONDecodeError:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid JSON format.'
            }, status=400)

        form = ProblemForm(data)  # Pass the parsed JSON data to the form
        if form.is_valid():
            problem = form.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Problem added successfully!',
                'problem': {
                    'title': problem.title,
                    'description': problem.description,
                    'difficulty': problem.difficulty,
                    'tag': problem.tag
                }
            }, status=201)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'Only POST requests are allowed.'
        }, status=405)