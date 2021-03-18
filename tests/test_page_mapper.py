from selenium.webdriver import Remote
from src import PageTodo

def browser_start():
    browser = Remote(
        desired_capabilities={
            'browserName': 'firefox',
            'browserTimeout': 10
        }
    )
    return browser

def create_task(name, description, driver):
    url = 'https://selenium.dunossauro.live/todo_list.html'
    page = PageTodo(driver, url)

    page.open()
    page.tasks.create_task(
        name,
        description
    )
    return (page.todo.tasks[0], page)

def test_browser_init():
    """
    Scene: browser is started
        Given the driver object
        when the browser is started
        then webdriver must be connected
        and the main page must be blank
    """
    browser = browser_start()

    assert browser.w3c == True
    assert browser.title == ''

    browser.quit()

def test_task_is_on_todo():
    """
    Scene: create a task
        Given you are on the todo page
        when a task is created
        then the task must be on the "Todo" tasks
    """
    browser = browser_start()
    first_task, _ = create_task('Just testing', 'Testing todo', browser)
    
    assert first_task.name == 'Just testing'
    assert first_task.description == 'Testing todo'
    
    browser.quit()

def test_task_should_be_on_doing():
    """
    Scene: move task to doing
        Given you are on the todo page
        when a task is created
        and the task is moved to doing
        then the task must be on the "Doing" tasks
    """
    browser = browser_start()
    first_task, page = create_task('Just testing', 'Testing doing', browser)
    first_task.do()
    first_task_doing = page.doing.tasks[0]
    
    assert first_task_doing.name == 'Just testing'
    assert first_task_doing.description == 'Testing doing'
    
    browser.quit()

def test_task_should_be_on_done():
    """
    Scene: move task to done
        Given you are on the todo page
        when a task is created
        and the task is moved to doing
        and the task is moved to done
        then the task must be on the "Done" tasks
    """
    browser = browser_start()
    _, page = create_task('Just testing', 'Testing done', browser)
    
    page.todo.tasks[0].do()
    page.doing.tasks[0].do()
    first_task_done = page.done.tasks[0]
    
    assert first_task_done.name == 'Just testing'
    assert first_task_done.description == 'Testing done'
    
    browser.quit()

def test_priority_task_is_first():
    """
    Scene: verify task priority
        Given you are on the todo page
        when a task is created
        and another task is created and marked with priority
        then the priority task must be on top
    """
    browser = browser_start()
    _, page = create_task('Testing first task', 'First task description', browser)
    page.tasks.create_task('Priority task', 'The second task is the priority one', urgent=True)

    assert page.todo.tasks[0].name == 'Priority task'
    assert page.todo.tasks[0].description == 'The second task is the priority one'
    assert page.todo.tasks[1].name == 'Testing first task'
    assert page.todo.tasks[1].description == 'First task description'
    
    browser.quit()
    