Coding (one file per class + main.py)

Person 1: Result and Student. That covers the shared validation helpers and getters/setters, is_passed, update_grade/update_absences, matches, average_grade, total_absences, is_at_risk, add/remove_result, and their dunders.
Person 2: Course and Teacher. Course needs averages, highest/lowest grade, pass_rate and add/remove_result. Teacher needs add_course, student_count, average_grade and course_summary. Both need dunders.
Person 3: School part 1, which is load_from_csv (the trickiest bit), add_student/course/teacher, find_student, remove_result and the dunders. This person also does requirements 1, 13 and 15.
Person 4: School part 2, which is average_grade, top_students, at_risk_students, search_results and sort_results. This person also writes main.py (the menu, try/except input handling, and wiring up all 15 requirements) and does the final test run.

How it runs: main.py calls School.load_from_csv("student_performance.csv") to get the list of schools with everything linked. Then a menu loop offers the 15 requirements, and each option calls the method listed after the → in section 7 of your report.

Reflection paper: each person writes about their own part (what they built, what was hard, what they learned). Person 1 also writes about teamwork, Person 2 about how the design changed in the code, and Person 3 about testing and bugs. Person 4 writes the intro and conclusion and edits it all into one voice.