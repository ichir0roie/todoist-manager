from asyncio import tasks
import time
import todoist_api_python.api as Todoist

import package.constants as cst
import package.settings as stg


from package.todoist_manager import TodoistManager

import datetime
import math
import random


class Test(TodoistManager):
    def __init__(self, mode_test: bool):
        super().__init__(mode_test)

        self.set_test_project()

    def set_test_project(self):
        for project in self.projects:
            if project.name == "TEST":
                self.test_project = project
                return
        self.create_test_project()

    def create_test_project(self):
        self.test_project = self.api.add_project(name="TEST")
        self.update_projects()

    def get_test_tasks(self):
        tasks = self.api.get_tasks(project_id=self.test_project.id)
        if len(tasks) < 5:
            tasks = self.create_test_tasks()
        return tasks

    def create_test_tasks(self):
        tasks = []
        for i in range(5):
            print()
            content = "test task {}".format(i)
            task = self.api.add_task(project_id=self.test_project.id, content=content)
            tasks.append(task)
        return tasks

    def run(self):
        self.set_test_project()
        print("test")
        test_tasks = self.get_test_tasks()
        print(test_tasks)


if __name__ == "__main__":
    cls = Test(mode_test=False)
    cls.run()
    pass
