with open("02.txt") as _:
    puzzle_input = _.read().strip()


reports = puzzle_input.split('\n')
reports = [list(map(int, report.split())) for report in reports]


def is_report_safe(report):
    differences = [item0 - item1 for item0, item1 in zip(report[:-1], report[1:])]
    is_increasing = sum(differences) > 0
    for difference in differences:
        if not 1 <= abs(difference) <= 3 or not (difference > 0) == is_increasing:
            return False
    return True


safe_reports_count = 0
for report in reports:
    if is_report_safe(report):
        safe_reports_count += 1

print(safe_reports_count)


def is_report_safe2(report, tolerate=True):
    differences = [item0 - item1 for item0, item1 in zip(report[:-1], report[1:])]
    is_increasing = sum(differences) > 0
    for index, difference in enumerate(differences):
        if not 1 <= abs(difference) <= 3 or not (difference > 0) == is_increasing:
            if tolerate:
                trial0 = report[:]
                trial0.pop(index)
                trial0 = is_report_safe2(trial0, tolerate=False)
                trial1 = report[:]
                trial1.pop(index+1)
                trial1 = is_report_safe2(trial1, tolerate=False)
                return any([trial0, trial1])
            else:
                return False
    return True


safe_reports_count = 0
for report in reports:
    if is_report_safe2(report):
        safe_reports_count += 1

print(safe_reports_count)