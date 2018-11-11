def task_scheduler(tasks, cooldown_time):
    # Idea: make a hashmap to store each integer's current time and decrement each time every interval?
    # Idea: make hashmap with integer id's as keys and the INDEX that the cooldown would be over as a value. No need to decrement that way
    index = intervals = 0
    task_map = dict()
    while index < len(tasks):
        task = tasks[index]
        time_to_wait = 0
        if task in task_map:
            time_to_wait = task_map[task]
            if index >= time_to_wait:
                intervals += 1
                task_map[task] = time_to_wait+cooldown_time+1
            elif index < time_to_wait:
                intervals += (time_to_wait - intervals) +1
                task_map[task] = time_to_wait+cooldown_time+1
        else:
            task_map[task] = intervals + cooldown_time + 1
            intervals += 1
        index += 1
    return intervals

print(task_scheduler([3,3,1,3], 2))
print(task_scheduler([3,4,5,3,4,5], 4))
