import json
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .forms import ProblemForm
from django.views.decorators.csrf import csrf_exempt
from .models import Problem
from submit.views import run_code
# Create your views here.

def problems_list(request):
    problems = Problem.objects.all()
    print(problems[0].description)
    context = {
        'problems':problems,
    }
    template = loader.get_template('all_problems.html')
   
    return HttpResponse(template.render(context,request))


def problem_detail(request, problem_id):
    
    problem = Problem.objects.get(id=problem_id)
    if request.method == 'POST':
        # Capture the user's submitted code
        user_code = request.POST.get('code')
        # Here you can pass the `user_code` to a function for processing
        result = run_code(user_code)  # Assume you have a function `run_code` to process the code
        print(result)
        # Render the template with the result or any feedback
        # return render(request, 'problem_detail.html', {
        #     'problem': problem,
        #     'result': result,  # Pass the result back to the template if needed
        # })
    
    
    
    context = {"problem":  problem}

    template = loader.get_template('problem_detail.html')
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