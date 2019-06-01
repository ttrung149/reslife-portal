from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from IRs.models import IR
from residencies.models import Resident


class IRListView(ListView):
    model = IR

    def get_queryset(self):
        return IR.objects.filter(author=self.request.user).order_by('-date_posted')


class IRDetailView(DetailView):
    model = IR


class IRCreateView(LoginRequiredMixin, CreateView):
    model = IR
    fields = ['title', 'student_ID', 'date_of_incident',
              'location', 'building', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user

        student_ID = self.request.POST.get('student_ID')
        resident = Resident.objects.filter(
            student_ID=student_ID)

        if resident:
            return super().form_valid(form)
        else:
            messages.warning(
                self.request, f'Student ID: {student_ID} is not found, try again!')
            return redirect('ir-create')
