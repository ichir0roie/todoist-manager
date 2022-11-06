
import todoist_api_python.api as Todoist

import package.todoist_constants as cst


from package.todoist_manager import TodoistManager, MyType


class RandomDueDate(TodoistManager):

    # get no date and not noDueDate and not subtask
    def get_tasks(self) -> MyType.ListTask:
        return self.api.get_tasks(
            filter="overdue & !@throwAway & (p3|p4)"
        )

    def edit_task(self, task: Todoist.Task):
        due_date = self.get_date_string(self.get_random_date(1, 7))
        self.api.update_task(task_id=task.id, due_date=due_date)
        return "overdue reset : {}".format(due_date)


if __name__ == "__main__":
    rdd = RandomDueDate(mode_test=False)
    rdd.run()
