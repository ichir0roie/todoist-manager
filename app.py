from operator import truediv
import sys

sys.path.insert(0, "package")
sys.path.insert(0, "scripts")

import test
import scripts.random_reschedule
import scripts.random_due_date


def run_due_date(mode_test):
    t = scripts.random_due_date.RandomDueDate(mode_test=mode_test)
    t.run()


def run_reschedule(mode_test):
    t = scripts.random_reschedule.RandomReschedule(mode_test=mode_test)
    t.run()


def handler(event: dict, context):
    print(event)
    print(context)
    if event is None:
        print("event is None")
        return

    if "mode" in event.keys():
        mode = event["mode"]
    else:
        raise Exception("mode is not set.")
    if "test" in event.keys():
        mode_test = event["test"]
    else:
        raise Exception("test is not set.")

    print("mode : {}\ntest : {}".format(mode, mode_test))

    if mode == "all":
        run_due_date(mode_test)
        run_reschedule(mode_test)
    elif mode == "random_due_date":
        run_due_date(mode_test)
    elif mode == "random_reschedule":
        run_reschedule(mode_test)


if __name__ == "__main__":
    handler(None, None)
    pass
