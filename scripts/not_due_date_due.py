import todoist_api_python.api as Todoist

import package.todoist_constants as cst


from package.todoist_manager import TodoistManager, MyType

# https://stackoverflow.com/questions/59814627/how-do-i-remove-the-due-date-from-a-todoist-item


class NotDueDateDue(TodoistManager):

    # get no date and not noDueDate and not subtask
    def get_tasks(self) -> MyType.ListTask:
        return self.api.get_tasks(
            filter="@notDueDate & ! no date"
        )

    def edit_task(self, task: Todoist.Task):
        self.api.update_task(
            task_id=task.id, due_string="no due date"
        )
        return "not due date"


if __name__ == "__main__":
    c = NotDueDateDue(mode_test=False)
    c.run()
