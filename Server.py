#Work in progress
def server_time_check(task_config, task_times):
  task_config = list(map(int, task_config.split()))
  task_times = list(map(int, task_times.split()))
  time = 0
  counter = 0
  for i in range(task_config[0]):
    time += task_times[i]
    if time < task_config[1]:
      counter += 1
    else:
      break
  return counter

## Please do not change the code below this line
## These lines are how the tests interact with the code

task_config = input()
task_times = input()

print(server_time_check(task_config, task_times))
