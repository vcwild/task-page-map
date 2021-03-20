Feature: Todo List
    Scenario: Create a task
        Given I am in the page "Todo"
        When Create a task
        """
            {
                "name": "Sleep",
                "description": "is so good"
            }
        """
        Then the task should be in heap "Todo"

    Scenario: Create many tasks
        Given I am in the page "Todo"
        When I create many tasks
            | name    | description     |
            | sleep   | is so good      |
            | eat     | some vegetables |
        Then there should be many tasks in the heap "Todo"
            | name    | description     |
            | sleep   | is so good      |
            | eat     | some vegetables |

    Scenario: Create a task with priority
        Given I am in the page "Todo"
        When I create many tasks with urgency flagged
            | name    | description     | urgent |
            | sleep   | is so good      | False  |
            | eat     | some vegetables | True   |
        Then the priority task must be on the top of the heap "Todo"
            | name    | description     |
            | eat     | some vegetables |
            | sleep   | is so good      |