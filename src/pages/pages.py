from ..page_objects.page_objects import Page
from .elements import Tasks, Todo, Doing, Done


class BasePage(Page):
    navbar = None


class PageTodo(BasePage):
    tasks = Tasks()
    todo = Todo()
    doing = Doing()
    done = Done()
