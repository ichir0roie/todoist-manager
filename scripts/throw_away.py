
import todoist_api_python.api as Todoist

import package.todoist_constants as cst


from package.todoist_manager import TodoistManager, MyType


class ThrowAway(TodoistManager):

    # get no date and not noDueDate and not subtask
    def get_tasks(self) -> MyType.ListTask:
        return self.api.get_tasks(
            filter="@throwAway"
        )

    def edit_task(self, task: Todoist.Task):
        due_date = self.get_date_string(self.get_random_date(1, 360))
        label_id = self.get_label_id(cst.LabelNames.auto_throw_away)
        self.api.update_task(task_id=task.id, due_date=due_date, label_ids=[label_id])
        return "throw away : {}".format(due_date)


if __name__ == "__main__":
    rdd = ThrowAway(mode_test=False)
    rdd.run()
