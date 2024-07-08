from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
import asyncio
from middlewares.main import SimpleMiddleWare
from django.utils.decorators import method_decorator

class MyView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'class_base_view_app/form.html', {'form': form})

    # Example of custom middleware
    @method_decorator(SimpleMiddleWare.simple_response)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User Created')
        return render(request, 'class_base_view_app/form.html', {'form': form})


class MyFirstView:
    async def get(self, request):
        await asyncio.sleep(1)
        return HttpResponse("Home......")
    