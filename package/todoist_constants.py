class Filter:
    reschedule = "((no date & !subtask ) | (#inbox & !subtask) )& !@notDueDate"
    overdue = "overdue & !@throwAway"
    throwAway = "@throwAway"


class LabelId:
    auto_due_date = 2161597893
    auto_reschedule = 2161597854
    auto_throw_away = 2161597866
    throw_away = 2161597200
