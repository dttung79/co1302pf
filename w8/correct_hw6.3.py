def main():
    goal = int(input('Enter number of steps for a week: '))
    n_steps, achieved = log_weekly(goal)
    print(f'Total steps: {n_steps}')
    print(f'Average daily steps: {n_steps / 7:.2f}')
    print(f'Weekly goal reached: {achieved}')

def log_weekly(goal):
    n_steps = 0
    for day in range(1, 8):
        n_steps += log_daily(day)
    achieved = 'yes' if n_steps >= goal else 'no'
    
    return n_steps, achieved

def log_daily(day):
    invalid = True
    while invalid:
        n_steps = int(input(f'Enter steps for Day {day}: '))
        if n_steps <= 0:
            print('Invalid number of steps. Please enter a positive number.')
        else:
            invalid = False
    return n_steps

####
main()