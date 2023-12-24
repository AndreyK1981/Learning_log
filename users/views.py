from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm


def logout_my(request):
    if request.method != 'POST':
        request.method = 'POST'
    else:
        pass
    logout(request)
    return redirect('learning_logs:index')

def register(request):
    """Регистрирует нового пользователя"""
    if request.method != 'POST':
        # Выводит пустую форму регистрации
        form = UserCreationForm
    else:
        # Обработка заполненной формы
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страницу
            login(request, new_user)
            return redirect('learning_logs:index')

    # Вывести пустую или недействительную форму
    context = {'form': form}
    return render(request, 'registration/register.html', context)