from asyncio import tasks
import time
import todoist_api_python.api as Todoist

import package.constants as cst
import package.settings as stg


from package.todoist_manager import TodoistManager

import datetime
import math
import random


class RandomDueDate(TodoistManager):

    # get no date and not noDueDate and not subtask
    def get_tasks_need_due_date(self):
        filter = "no date & !@noDueDate & !subtask"
        tasks = self.api.get_tasks(filter=filter)
        return tasks

    def run(self):
        tasks = self.get_tasks_need_due_date()
        self.set_random_due_date(tasks=tasks)
        print("finish")


if __name__ == "__main__":
    rdd = RandomDueDate()
    # rdd.test()
    rdd.run()
    pass
