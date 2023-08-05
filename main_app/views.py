from django.shortcuts import render

finches = [
  {'name': 'Lolo', 'breed': 'House Finch', 'description': 'lovely voice', 'age': 3},
  {'name': 'Sachi', 'breed': 'Red Crosbill', 'description': 'gentle and loving', 'age': 2},
  {'name': 'Tweety', 'breed': 'American Goldfinch', 'description': '... what will I be? Will I be pretty?', 'age': 0},
]

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(req):
    return render(req, 'about.html')

def index(req):
    return render(req,'finches/index.html',{
        'finches': finches,
    })