import json

def add_task():
    new_task = input('Add your task : ')
    new_prio = input('Add your priority [High/Low/Medium] : ')
    if new_prio == 'High' or new_prio == 'Low' or new_prio == 'Medium':
        new_doc = {
            'task': new_task,
            'priority': new_prio,
            'status': 'To Do'
        }

        with open('task.txt', 'a') as file:
            task_json = json.dumps(new_doc)
            file.writelines(task_json + '\n')
            print('Task added successfully.')
    else:
        print('Please input correct priority.')

def change_status():
    task = input('Input task to change status: ')
    t_all = []
    old_status = ''
    new_status = ''
    with open('task.txt', 'r') as file_r:
        all_task = file_r.readlines()
        for t in all_task:
            t_temp = json.loads(t)
            if task == t_temp['task']:
                
                # set old status
                old_status = t_temp['status']

                if t_temp['status'] == 'To Do':
                    t_temp['status'] = 'In Progress'
                elif t_temp['status'] == 'In Progress':
                    t_temp['status'] = 'Finished'
                elif t_temp['status'] == 'Finished':
                    print('Task already finished.')

                # set new status
                new_status = t_temp['status']
            
            # to save all previous value    
            t_all.append(f'{json.dumps(t_temp)}\n')
    
    with open('task.txt', 'w') as file_w:
        file_w.writelines(t_all)
        if old_status == new_status:
            print(f'Task {task} not changed. Status : {new_status}')
        else:
            print(f'Task {task} status changed from {old_status} to {new_status}')

def view_all():
    with open('task.txt', 'r') as file:
        print('All Task')
        print('Task | Priority | Status')
        print('------------------------------')
        all_task = file.readlines()
        
        # if task is empty
        if len(all_task) == 0:
            print('No Task Available.')
        else:
            for t in all_task:
                t_temp = json.loads(t)
                print(f'{t_temp["task"]} | {t_temp["priority"]} | {t_temp["status"]}')
            
def view_specific_task():
    status = input('Input status task: ')
    with open('task.txt', 'r') as file:
        print(f'Task - {status}')
        print('Task | Priority | Status')
        print('------------------------------')
        all_task = file.readlines()
        counter = 0
        # if task is empty
        if len(all_task) == 0:
            print('No Task Available.')
        else:
            for t in all_task:
                t_temp = json.loads(t)
                if t_temp['status'] == status:
                    print(f'{t_temp["task"]} | {t_temp["priority"]} | {t_temp["status"]}')
                    counter += 1
            if counter == 0:
                print(f'No Task On Status {status}')

def delete_task():
    task = input('Input task to delete : ')
    
    # Before Delete
    print('Before Delete')
    view_all()

    t_all = []
    with open('task.txt', 'r') as file_r:
        all_task = file_r.readlines()
        for t in all_task:
            t_temp = json.loads(t)
            if t_temp['task'] != task:
                t_all.append(f'{json.dumps(t_temp)}\n')
    
    with open('task.txt', 'w') as file_w:
        file_w.writelines(t_all)
        if len(t_all) == len(all_task):
            print('\nNo Task Deleted, please input correct task.\n')
        else:
            print('\nTask successfully deleted.\n')

    # After Delete
    print('After Delete')
    view_all()

def display_percentage():
    with open('task.txt', 'r') as file_r:
        all_task = file_r.readlines()
        
        total_task = len(all_task)
        to_do = 0
        in_progress = 0
        finished = 0

        for t in all_task:
            t_temp = json.loads(t)
            if t_temp['status'] == 'Finished':
                finished += 1
            elif t_temp['status'] == 'To Do':
                to_do += 1
            elif t_temp['status'] == 'In Progress':
                in_progress += 1
        print(f'All Task : {total_task}')
        print(f'To Do Task : {to_do}')
        print(f'In Progress Task : {in_progress}')
        print(f'Finished Task : {finished}')
        print(f'Percentage Finished Task : {finished/total_task * 100}%')

while True:
    print('Menu:')
    print('1. Add Task')
    print('2. Change Task Status')
    print('3. View All Task')
    print('4. View Specific Task')
    print('5. Delete Task')
    print('6. Display Percentage Finished Task')
    print('7. Exit')

    menu = int(input("Select menu : "))
    if menu == 1:
        add_task()
    elif menu == 2:
        change_status()
    elif menu == 3:
        view_all()
    elif menu == 4:
        view_specific_task()
    elif menu == 5:
        delete_task()
    elif menu == 6:
        display_percentage()
    elif menu == 7:
        print('Exit.')
        break
    else:
        print('Invalid Menu')