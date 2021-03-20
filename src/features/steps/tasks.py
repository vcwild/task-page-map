from behave import given, when, then
import json
from src.pages import PageTodo


@given('I am in the page {page}')
def go_to_page(context, page):
    context.page = PageTodo(
        context.browser, 
        'http://selenium.dunossauro.live/todo_list.html'
    )
    context.page.open()

@when('Create a task')
def create_task(context):
    task_text = json.loads(context.text)
    context.page.tasks.create_task(
        name=task_text['name'],
        description=task_text['description']
    )

@when('I create many tasks')
def create_many_tasks(context):
    for r in context.table.rows:
        row = dict(r.items()) 
        context.page.tasks.create_task(
            name=row['name'],
            description=row['description']
        )

@when('I create many tasks with urgency flagged')
def create_many_tasks_with_urgency_flag(context):
    for r in context.table.rows:
        row = dict(r.items()) 
        context.page.tasks.create_task(
            name=row['name'],
            description=row['description'],
            urgent=bool(row['urgent'])
        )

@then('the task should be in heap "{heap}"')
def check_task(context, heap):
    element = heap.lower().replace(' ', '_')
    page_element = getattr(context.page, element)
    assert 1 == len(page_element.tasks)

@then('there should be many tasks in the heap "{heap}"')
def check_many_tasks(context, heap):
    element = heap.lower().replace(' ', '_')
    page_element = getattr(context.page, element)
    table_items = [dict(i.items()) for i in context.table.rows]
    assert page_element.tasks[0].name == table_items[0]['name']
    assert page_element.tasks[1].name == table_items[1]['name']

@then('the priority task must be on the top of the heap "{heap}"')
def check_priority_task(context,heap):
    element = heap.lower().replace(' ', '_')
    page_element = getattr(context.page, element)
    table_items = [dict(i.items()) for i in context.table.rows]
    assert page_element.tasks[0].name == table_items[0]['name']
    assert page_element.tasks[1].name == table_items[1]['name']
