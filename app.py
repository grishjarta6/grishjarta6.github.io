import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Мое веб-приложение на Python"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Переменные состояния
    counter = 0
    todos = []
    
    # Функция для счетчика
    def increment_counter(e):
        nonlocal counter
        counter += 1
        counter_text.value = f"Счетчик: {counter}"
        page.update()
    
    # Функция для добавления задачи
    def add_todo(e):
        if todo_input.value:
            todos.append(todo_input.value)
            todo_list.controls.append(
                ft.ListTile(
                    title=ft.Text(todo_input.value),
                    leading=ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE),
                    on_click=lambda e, t=todo_input.value: remove_todo(t)
                )
            )
            todo_input.value = ""
            todo_counter.value = f"Всего задач: {len(todos)}"
            page.update()
    
    # Функция для удаления задачи
    def remove_todo(todo_text):
        if todo_text in todos:
            todos.remove(todo_text)
            todo_list.controls = [
                c for c in todo_list.controls 
                if c.title.value != todo_text
            ]
            todo_counter.value = f"Всего задач: {len(todos)}"
            page.update()
    
    # Функция для показа текущего времени
    def show_time(e):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        time_display.value = f"Текущее время: {current_time}"
        page.update()
    
    # Создаем элементы интерфейса
    
    # Заголовок
    title = ft.Text(
        "Добро пожаловать в Flet приложение!",
        size=32,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLUE_700
    )
    
    subtitle = ft.Text(
        "Этот Python код выполняется прямо в вашем браузере",
        size=16,
        color=ft.colors.GREY_600
    )
    
    # Секция счетчика
    counter_text = ft.Text("Счетчик: 0", size=24)
    counter_btn = ft.ElevatedButton(
        "Увеличить счетчик",
        icon=ft.icons.ADD,
        on_click=increment_counter,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.BLUE_400,
            color=ft.colors.WHITE
        )
    )
    
    # Секция времени
    time_display = ft.Text("Нажмите кнопку, чтобы узнать время", size=18)
    time_btn = ft.ElevatedButton(
        "Показать время",
        icon=ft.icons.ACCESS_TIME,
        on_click=show_time,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_400,
            color=ft.colors.WHITE
        )
    )
    
    # Секция списка дел
    todo_input = ft.TextField(
        label="Новая задача",
        hint_text="Введите задачу...",
        expand=True,
        border_color=ft.colors.BLUE_300
    )
    
    add_btn = ft.IconButton(
        icon=ft.icons.ADD_CIRCLE,
        icon_color=ft.colors.BLUE_500,
        on_click=add_todo
    )
    
    todo_counter = ft.Text("Всего задач: 0", size=16, color=ft.colors.GREY_600)
    
    todo_list = ft.ListView(
        spacing=10,
        height=200
    )
    
    # Располагаем элементы на странице
    page.add(
        ft.Column([
            ft.Container(
                content=ft.Column([
                    title,
                    subtitle,
                    ft.Divider(height=30, color=ft.colors.TRANSPARENT)
                ]),
                alignment=ft.alignment.center
            ),
            
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Счетчик", size=20, weight=ft.FontWeight.BOLD),
                        counter_text,
                        counter_btn
                    ], spacing=15),
                    padding=20
                ),
                elevation=5
            ),
            
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Текущее время", size=20, weight=ft.FontWeight.BOLD),
                        time_display,
                        time_btn
                    ], spacing=15),
                    padding=20
                ),
                elevation=5
            ),
            
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Список дел", size=20, weight=ft.FontWeight.BOLD),
                        ft.Row([todo_input, add_btn]),
                        todo_counter,
                        todo_list
                    ], spacing=15),
                    padding=20
                ),
                elevation=5
            ),
            
            ft.Container(
                content=ft.Column([
                    ft.Divider(),
                    ft.Text(
                        "✨ Все работает в браузере без сервера!",
                        size=14,
                        color=ft.colors.GREY_500,
                        text_align=ft.TextAlign.CENTER
                    )
                ]),
                padding=20
            )
        ], spacing=25)
    )

# Запускаем приложение
ft.app(target=main)
