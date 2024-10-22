from django.urls import path
from solveproblems.views import problems_list,problem_detail, add_problem

urlpatterns = [
    path("problems/", problems_list, name="problems-list"),
    path("problems/<int:problem_id>/", problem_detail, name="problem_detail"),
    path("problems/add/", add_problem, name="add_problem"),
]
