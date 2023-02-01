from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, permissions
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    UpdateView,
    CreateView,
    DeleteView
)
from .models import Snack, MyForm
# from rest_framework import generics
from .serializers import SnackSerializer
from .permissions import IsOwnerOrReadOnly


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class SnackListView(ListView):
    template_name = 'pages/list.html'
    model = Snack
    context_object_name = 'snacks'


class SnackDetailView(DetailView):
    template_name = 'pages/detail.html'
    model = Snack


class SnackUpdateView(UpdateView):
    template_name = 'pages/update.html'
    model = Snack
    fields = "__all__"


class SnackCreateView(CreateView):
    template_name = 'pages/create.html'
    model = Snack
    fields = ["name", "rating", "reviewer", "image_url"]  # fields = "__all__" for all fields
    success_url = reverse_lazy("list")


class SnackDeleteView(DeleteView):
    template_name = 'pages/delete.html'
    model = Snack
    success_url = reverse_lazy("list")


def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            success_url = reverse_lazy("list")
            return HttpResponseRedirect(success_url)
    else:
        form = MyForm()
    return render(request, 'pages/create.html', {'form': form})


# class SnackAPIListView(generics.ListAPIView):
#     queryset = Snack.objects.all()
#     serializer_class = SnackSerializer
#
#
# class SnackAPIDetailView(generics.RetrieveAPIView):
#     queryset = Snack.objects.all()
#     serializer_class = SnackSerializer

class SnackViewSet(viewsets.ModelViewSet):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = [permissions.IsAuthenticated]
    permission_classes = (IsOwnerOrReadOnly,)
