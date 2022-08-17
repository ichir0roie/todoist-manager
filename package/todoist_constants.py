class Filter:
    reschedule = "((no date & !subtask ) | (#inbox & !subtask) )& !@notDueDate"
    overdue = "overdue & !@throwAway"
    throw_away = "@throwAway"
    not_due_date_due = "@notDueDate & ! no date"


class LabelNames:
    throw_away = "throwAway"
    not_due_date = "notDueDate"
    auto_throw_away = "Auto:ThrowAway"
    auto_Reschedule = "Auto:Reschedule"
    auto_due_date = "Auto:DueDate"
