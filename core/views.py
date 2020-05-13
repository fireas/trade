from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.conf import settings
from django.http import Http404

from .models import Book
from .forms import AddForm
from .filers import BFilter



# Create your views here.
class FilterHomeView(ListView):
    filterset_class = BFilter

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filter'] = BFilter(self.request.GET, queryset=self.get_queryset())
        return context

class HomeView(FilterHomeView):
    model = Book
    paginate_by = 4
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['home_active'] = 'active'
        return context

class BookDetailView(DetailView):
    model = Book
    template_name = "book.html"

def checkout_view(request):
    context = {
        'books' : Book.objects.all()
    }
    return render(request,'checkout.html',context)

def addBook_view(request):
    if not request.user.is_authenticated:
        raise Http404

    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('core:home')
    else:
        form = AddForm()

    context = {
        'form': form,
        'addbook_active':'active'
    }
    return render(request, 'addbook.html', context)



class MyBooksView(LoginRequiredMixin, ListView):
    model = Book
    paginate_by = 4
    template_name = "mybooks.html"
    login_url = 'accounts/login/'
    redirect_field_name = 'redirect_to'
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['mybooks_active'] = 'active'
        return context




