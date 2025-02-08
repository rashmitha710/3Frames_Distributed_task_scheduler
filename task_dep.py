

##2
from collections import defaultdict

task_dependencies = defaultdict(list)  # {task_A: [task_B, task_C]}

def add_dependency(task_A, task_B):
    task_dependencies[task_A].append(task_B)

def execute_task(task_id):
    if task_id in task_dependencies:
        for dependent_task in task_dependencies[task_id]:
            add_task(dependent_task, {"depends_on": task_id})
