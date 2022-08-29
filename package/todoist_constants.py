class Filter:
    reschedule = "no date & !subtask & !@notDueDate"
    overdue = "overdue & !@throwAway & (p3|p4)"
    throw_away = "@throwAway"
    due_not_due_date = "@notDueDate & ! no date"


class LabelNames:
    throw_away = "throwAway"
    not_due_date = "notDueDate"
    auto_throw_away = "Auto:ThrowAway"
    auto_Reschedule = "Auto:Reschedule"
    auto_due_date = "Auto:DueDate"
