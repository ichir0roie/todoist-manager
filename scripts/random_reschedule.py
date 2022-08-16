from asyncio import tasks
import time
import todoist_api_python.api as Todoist

import package.todoist_constants as cst
import package.settings as stg

from package.todoist_manager import TodoistManager, MyType
import package.todoist_constants as cst

import datetime
import math
import random


class RandomReschedule(TodoistManager):
    def get_tasks(self) -> MyType.ListTask:
        return self.api.get_tasks(filter=cst.Filter.reschedule)

    def edit_task(self, task: Todoist.Task):
        due_date = self.get_date_string(self.get_random_date(1, 90))
        self.api.update_task(
            task_id=task.id, due_date=due_date, label_ids=[cst.LabelId.auto_reschedule]
        )


if __name__ == "__main__":
    rr = RandomReschedule(mode_test=False)
    # rr.test()
    rr.run()
    pass
