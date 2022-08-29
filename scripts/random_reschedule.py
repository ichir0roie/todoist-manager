import todoist_api_python.api as Todoist

import package.todoist_constants as cst

from package.todoist_manager import TodoistManager, MyType
import math


class RandomReschedule(TodoistManager):
    def get_tasks(self) -> MyType.ListTask:
        return self.api.get_tasks(filter=cst.Filter.reschedule)

    def edit_task(self, task: Todoist.Task):
        range_min = int((task.priority - 1) * 7 * math.pow(1.5, task.priority - 2))
        range_max = int((task.priority - 0) * 7 * math.pow(1.5, task.priority - 1))
        due_date = self.get_date_string(
            self.get_random_date(range_start=range_min, range_end=range_max)
        )
        label_id = self.get_label_id(cst.LabelNames.auto_Reschedule)
        self.api.update_task(task_id=task.id, due_date=due_date, label_ids=[label_id])
        return "reschedule : {}".format(due_date)


if __name__ == "__main__":
    rr = RandomReschedule(mode_test=False)
    # rr.test()
    rr.run()
    pass
