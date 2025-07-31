
import json
import os
from datetime import date



def add_task(topic, description, due):
    if os.path.exists('tasks.json') and os.path.getsize('tasks.json') > 0:
        with open('tasks.json', 'r', encoding='utf-8') as f:

            file_data = json.load(f)
            if file_data is not None:
                tasks_list = [data for data in file_data]
            else:
                tasks_list = []

            task = {
                    'topic': f'{topic}',
                    'description': f'{description}',
                    'date': f'{date.today()}',
                    'due': f'{due}',
                    'is_complete': False
                }

        tasks_list.append(task)

        with open('tasks.json', 'w', encoding='utf-8') as f:
            json.dump(tasks_list, f, indent=4)
            print(f'Task {topic} Added!')
    
    else:
        file_data = []
        with open('tasks.json', 'w', encoding='utf-8') as f:
            json.dump(file_data, f)
            print('try again!!')

def remove_tasks(topic):
    try:
        if os.path.exists('tasks.json') and os.path.getsize('tasks.json') > 0:
            with open('tasks.json', 'r', encoding='utf-8') as tasks:
                data = json.load(tasks)
                found = False
                for task_ in data:
                    if task_['topic'] == f'{topic}':
                        data.remove(task_)
                        with open('tasks.json', 'w', encoding='utf-8') as tasks:
                            json.dump(data, tasks, indent=4)
                            print('Task removed!')
                            found = True
                            break
                    if found:
                        print('Task doesnt exist')
        else:
            data = []
            with open('tasks.json', 'w', encoding='utf-8') as f:
                json.dump(data, f)
                print('try again!!')


    except FileNotFoundError as err:
        print(err)

def mark_done(topic):
    try:
        if os.path.exists('tasks.json') and os.path.getsize('tasks.json') > 0:
            with open('tasks.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                for task in data:
                    if task['topic'] == topic and task['is_complete'] == False:
                        task['is_complete'] = True

                        with open('tasks.json', 'w', encoding='utf-8') as f:
                            json.dump(data, f, indent=4)

                    elif task['topic'] == topic and task['is_complete'] == True:
                        print('Task is Marked as done already')
                    else:
                        print('something went wrong')
        else:
            data = []
            with open('tasks.json', 'w', encoding='utf-8') as f:
                json.dump(data, f)
                print('try again!!')



    except FileNotFoundError as err:
        print(err)


def show_menu():

    print('**********To Do List*******')
    try:
        if os.path.exists('tasks.json') and os.path.getsize('tasks.json') > 0:
            with open('tasks.json', 'r', encoding='utf-8') as f:
                data = json.load(f)

                if data:
                    for tasks in data:
                        topic = tasks.get('topic')
                        description = tasks.get('description')
                        due = tasks.get('due')
                        if tasks.get('is_complete'):
                            print('topic: ' + topic + ' [DONE]') 
                            print('description: ' + description)
                            print(f'due: {due}')
                            print('******************************************************')
                        else:
                            print('topic: ' + topic) 
                            print('description: ' + description)
                            print(f'due: {due}')
                            print('******************************************************')

                else:
                    print("Theres no current tasks added")
        else:
            data = []
            with open('tasks.json', 'w', encoding='utf-8') as f:
                json.dump(data, f)
                print('try again!!')

        
    except FileNotFoundError as e:
        print(f'error: {e}')


def main():
    print(
        '''
1: add tasks
2: remove tasks
3: mark as done
4: show tasks
5: close program
'''
)
    
    while True:
        choice = input('choice: ')

        if choice == "" '1':
            topic = input('Topic: ')
            description = input('description: ')
            due = input('Due date (20250802): ')


            year, month, day = int(due[0:4]), int(due[4:6]), int(due[6:8])
            try:
                due_date = date(year, month, day)
            except Exception:
                print('invalid date')

            add_task(topic, description, due_date)
            show_menu()

        elif choice == '2':
            show_menu()
            topic = input('Task to remove: ')
            remove_tasks(topic)
            
        elif choice == '3':
            show_menu()
            topic = input('Topic to mark as done: ')
            mark_done(topic)
            show_menu()

        elif choice == '4':
            show_menu()

        elif choice == '5':
            break

        else:
            print('invalid choice')


if __name__ == '__main__':
    os.system('clear')
    main()