from todoist_api_python.api import TodoistAPI
import todoist_api_python.api as Todoist


import package.settings as stg

import datetime
import time
import random
import math


class MyType:
    ListTask = list[Todoist.Task]


class TodoistManager:
    def __init__(self, mode_test: bool):
        self.api = TodoistAPI(stg.token)
        self.projects = None
        self.update_projects()
        self.mode_test = mode_test

        return

    def update_projects(self):
        try:
            self.projects = self.api.get_projects()
            # print(self.projects)
        except Exception as error:
            print(error)

    def update_task_date(task: Todoist.Task, date: datetime.datetime):
        due_date = date.strftime("%Y-%m-%d")
        time.sleep(1)

    def set_random_due_date(self, tasks: list[Todoist.Task]):
        for task in tasks:
            due_date = self.get_random_date_by_priority(task.priority)
            if not self.mode_test:
                self.api.update_task(
                    task_id=task.id, due_date=self.get_date_string(due_date)
                )
            else:
                print("test mode : set due {} to {}".format(task.id, task.due))
                print(task.id)
            print("{} : {}".format(task.content, due_date))
            time.sleep(1)

    def get_random_date_by_priority(self, priority: int) -> datetime.datetime:
        add_date_base = 7
        add_date = math.pow(priority, 2) * add_date_base
        add_random = add_date_base + random.randint(0, add_date)
        return self.get_random_date(0, add_random)

    def get_random_date(self, range_start: int, range_end) -> datetime.datetime:
        date = datetime.datetime.now()
        date = date + datetime.timedelta(days=random.randint(range_start, range_end))
        return date

    def get_date_string(self, date: datetime.datetime) -> str:
        return date.strftime("%Y-%m-%d")

    def run(self):
        task_list = self.get_tasks()
        self._edit_tasks(task_list=task_list)

    def get_tasks(self) -> MyType.ListTask:
        return

    def _edit_tasks(self, task_list: MyType.ListTask):
        for task in task_list:
            self.edit_task(task)

    def edit_task(self, task: Todoist.Task):
        pass


if __name__ == "__main__":
    print("main")
    tm = TodoistManager()
    tm.test()
