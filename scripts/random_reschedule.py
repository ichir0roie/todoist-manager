from asyncio import tasks
import time
import todoist_api_python.api as Todoist

import package.constants as cst
import package.settings as stg


from package.todoist_manager import TodoistManager

import datetime
import math
import random


class RandomReschedule(TodoistManager):

    # get no date and not noDueDate and not subtask
    def get_tasks_filter(self):
        filter = "overdue"
        tasks = self.api.get_tasks(filter=filter)
        return tasks

    def run(self):
        tasks = self.get_tasks_filter()
        self.set_random_due_date(tasks=tasks)


if __name__ == "__main__":
    rr = RandomReschedule()
    # rr.test()
    rr.run()
    pass
