from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import request
from .models import Post
from .forms import UserRegistration, UserEditForm

# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

@login_required
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

@login_required
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


@login_required
def dashboard(request):
    context = {
        "welcome": "Welcome to your dashboard"
    }
    return render(request, '../dashboard.html', context=context)

@login_required
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, '../register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, '../register.html', context=context)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'form': user_form,
    }
    return render(request, '../edit.html', context=context)



