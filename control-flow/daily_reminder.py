task = input("Describe the task: ")
priority = input("What's the tasks priority (high, medium, low): ")
time_bound = input("Is the task time bound (yes or no)? ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention!")
        elif time_bound == "no":
            print(f"Note: {task} is a high priority task that doesn't require immediate attention")
        else:
            print("Input the correct time-bound condition.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that requires immediate attention!")
        elif time_bound == "no":
            print(f"Note: {task} is a medium priority task that doesn't require immediate attention")
        else:
                print("Input the correct time-bound condition.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a low priority task that requires immediate attention!")
        elif time_bound == "no":
            print(f"Note: {task} is a low priority task that doesn't require immediate attention")
        else:
            print("Input the correct time-bound condition.")
    case _:
            print("Please input a valid priority string.")