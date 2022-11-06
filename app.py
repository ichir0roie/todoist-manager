import sys

sys.path.insert(0, "package")
sys.path.insert(0, "scripts")

from scripts.random_reschedule import RandomReschedule
from scripts.random_due_date import RandomDueDate
from scripts.throw_away import ThrowAway
from scripts.not_due_date_due import NotDueDateDue

import json


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

    result = []

    if mode == "all":
        # result.append(RandomDueDate(mode_test=mode_test).run())
        result.append(RandomReschedule(mode_test=mode_test).run())
        result.append(ThrowAway(mode_test=mode_test).run())
        result.append(NotDueDateDue(mode_test=mode_test).run())
    if "random_due_date" in mode:
        RandomDueDate(mode_test=mode_test).run()
    if "random_reschedule" in mode:
        RandomReschedule(mode_test=mode_test).run()
    if "throw_away" in mode:
        ThrowAway(mode_test=mode_test).run()

    return json.dumps(result)
