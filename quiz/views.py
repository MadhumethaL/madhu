count =0
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usersdata,Score
from .forms import UserForm
from django.contrib.auth.decorators import login_required 
@login_required 


def index(request):
    return render(request, 'index.html')
def C(request):
    return render(request, 'C.html')
def ML(request):
    return render(request, 'ML.html')
def Python(request):
    return render(request, 'Python.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def prize(request):
    return render(request, 'prize.html')

def contact(request):
    return render(request, 'contact.html')

def Guides(request):
    return render(request, 'Guides.html')

def Timings(request):
    return render(request, 'Timings.html')

def info(request):
    return render(request, 'info.html')

def Outreach(request):
    return render(request, 'Outreach.html')

def leaderboard(request):
    return render(request, 'leaderboard.html')


def submit_answers(request):
    count=0
    if request.method == 'POST':
     
        q1_answer = request.POST.get('q1', '')
        q2_answer = request.POST.get('q2', '')
        q3_answer = request.POST.get('q3', '')
        q4_answer = request.POST.get('q4', '')
        q5_answer = request.POST.get('q5', '')

        correct_answers = {
            'q1': 'a', 
            'q2': 'a',  
            'q3': 'a', 
            'q4': 'b', 
            'q5': 'a', 
        }

        results = {}
        if q1_answer == correct_answers['q1']:
            results['q1'] = 'Correct'
            count+=1
        else:
            results['q1'] = 'Incorrect'

        if q2_answer == correct_answers['q2']:
            results['q2'] = 'Correct'
            count+=1
        else:
            results['q2'] = 'Incorrect'

        if q3_answer == correct_answers['q3']:
            results['q3'] = 'Correct'
            count+=1
        else:
            results['q3'] = 'Incorrect' 
            
        if q4_answer == correct_answers['q4']:
            results['q4'] = 'Correct'
            count+=1
        else:
            results['q4'] = 'Incorrect' 
            
        if q5_answer == correct_answers['q5']:
            results['q5'] = 'Correct'
            count+=1
        else:
            results['q5'] = 'Incorrect'

        context = {
            'results': results,
            'correct_answers': correct_answers,
            'count' : count
        }
        Username=Usersdata.objects.all().last()
        point=count
        var_instance=Score(Username=Username,points=point)
        var_instance.save()


        return render(request, 'submit_answers.html', context)

    return HttpResponse('Invalid request method')



def submit1_answers(request):
    count=0
    if request.method == 'POST':
     
        q1_answer = request.POST.get('q1', '')
        q2_answer = request.POST.get('q2', '')
        q3_answer = request.POST.get('q3', '')
        q4_answer = request.POST.get('q4', '')
        q5_answer = request.POST.get('q5', '')

        correct_answers = {
            'q1': 'c', 
            'q2': 'd',  
            'q3': 'b', 
            'q4': 'c', 
            'q5': 'a', 
        }

        results = {}
        if q1_answer == correct_answers['q1']:
            results['q1'] = 'Correct'
            count+=1
        else:
            results['q1'] = 'Incorrect'

        if q2_answer == correct_answers['q2']:
            results['q2'] = 'Correct'
            count+=1
        else:
            results['q2'] = 'Incorrect'

        if q3_answer == correct_answers['q3']:
            results['q3'] = 'Correct'
            count+=1
        else:
            results['q3'] = 'Incorrect' 
            
        if q4_answer == correct_answers['q4']:
            results['q4'] = 'Correct'
            count+=1
        else:
            results['q4'] = 'Incorrect' 
            
        if q5_answer == correct_answers['q5']:
            results['q5'] = 'Correct'
            count+=1
        else:
            results['q5'] = 'Incorrect'

        context = {
            'results': results,
            'correct_answers': correct_answers,
            'count':count,
        }
        Username=Usersdata.objects.all().last()
        point=count
        var_instance=Score(Username=Username,points=point)
        var_instance.save()
        return render(request, 'submit1_answers.html', context)

    return HttpResponse('Invalid request method')


def submit2_answers(request):
    count=0
    if request.method == 'POST':
     
        q1_answer = request.POST.get('q1', '')
        q2_answer = request.POST.get('q2', '')
        q3_answer = request.POST.get('q3', '')
        q4_answer = request.POST.get('q4', '')
        q5_answer = request.POST.get('q5', '')

        correct_answers = {
            'q1': 'c', 
            'q2': 'd',  
            'q3': 'b', 
            'q4': 'c', 
            'q5': 'a', 
        }

        results = {}
        if q1_answer == correct_answers['q1']:
            results['q1'] = 'Correct'
            count+=1
        else:
            results['q1'] = 'Incorrect'

        if q2_answer == correct_answers['q2']:
            results['q2'] = 'Correct'
            count+=1
        else:
            results['q2'] = 'Incorrect'

        if q3_answer == correct_answers['q3']:
            results['q3'] = 'Correct'
            count+=1
        else:
            results['q3'] = 'Incorrect' 
            
        if q4_answer == correct_answers['q4']:
            results['q4'] = 'Correct'
            count+=1
        else:
            results['q4'] = 'Incorrect' 
            
        if q5_answer == correct_answers['q5']:
            results['q5'] = 'Correct'
            count+=1
        else:
            results['q5'] = 'Incorrect'

        context = {
            'results': results,
            'correct_answers': correct_answers,
            'count':count,
        }
        
        return render(request, 'submit2_answers.html', context)
        Username=Usersdata.objects.all().last()
        point=count
        var_instance=Score(Username=Username,points=point)
        var_instance.save()
    return HttpResponse('Invalid request method')


def Login(request):
    form=UserForm(request.POST)
    if form.is_valid():
            form.save()
            return redirect("index")
    context={"uf":UserForm()}
    return render(request, 'Login.html',context)


def leaderboard(request):
    leaderboard_data = Score.objects.order_by('-points')[:10]  
    return render(request, 'leaderboard.html', {'leaderboard_data': leaderboard_data})


