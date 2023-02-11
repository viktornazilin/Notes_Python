from datetime import datetime

from Controller import controller
from Model import note


class View:
    def __init__(self, _controller):
        self.__controller = _controller

    def run(self):
        while True:
            command = str(input('Enter the command (help - list of all commands): '))
            if command.lower() == 'exit':
                return

            if command.lower() == 'create':
                title = str(input('Enter note title: '))
                msg = str(input('Enter note text: '))
                if isinstance(self.__controller, controller.Controller):
                    self.__controller.save_note(note.Note('0', title, msg, str(datetime.now().strftime("%Y.%m.%d %H:%M:%S"))))
                else:
                    print('Internal error!')

            elif command.lower() == 'read':
                note_id = str(input('Enter ID: '))
                if isinstance(self.__controller, controller.Controller):
                    _note = self.__controller.read_note(note_id)
                    print(f'ID: {_note.get_id()}')
                    print(f'Title: {_note.get_title()}')
                    print(f'Message: {_note.get_msg()}')
                    print(f'Date modified: {_note.get_date()}')
                else:
                    print('Internal error!')

            elif command.lower() == 'list':
                if isinstance(self.__controller, controller.Controller):
                    notes = self.__controller.read_notes()
                    notes.sort()
                    for _note in notes:
                        print(_note)
                else:
                    print('Internal error')

            elif command.lower() == 'find':
                while True:
                    date_start = input('Enter start date in format "YYYY.MM.DD HH:MM:SS": ')
                    try:
                        datetime.strptime(date_start, '%Y.%m.%d %H:%M:%S')
                        break
                    except:
                        print('Wrong date input format! Try again!')
                while True:
                    date_end = input('Enter end date in format "YYYY.MM.DD HH:MM:SS": ')
                    try:
                        datetime.strptime(date_end, '%Y.%m.%d %H:%M:%S')
                        break
                    except:
                        print('Wrong date input format! Try again!')
                if isinstance(self.__controller, controller.Controller):
                    notes = self.__controller.find_notes_by_date(date_start, date_end)
                    notes.sort()
                    for _note in notes:
                        print(_note)
                else:
                    print('Internal error!')

            elif command.lower() == 'delete':
                note_id = str(input('Enter ID: '))
                if isinstance(self.__controller, controller.Controller):
                    self.__controller.delete_note(note_id)
                else:
                    print('Internal error!')

            elif command.lower() == 'edit':
                note_id = str(input('Enter ID: '))
                title = str(input('Enter note title: '))
                msg = str(input('Enter note text: '))
                if isinstance(self.__controller, controller.Controller):
                    self.__controller.edit_note(note.Note(note_id, title, msg, str(datetime.now().strftime("%Y.%m.%d %H:%M:%S"))))

            elif command.lower() == 'help':
                print('List of commands:')
                print('list - display list of all notes')
                print('read - display note by ID')
                print('find - find note by date')
                print('create - create new note')
                print('edit - edit note by ID')
                print('delete - delete note by ID')
                print('exit - exit from program')
            else:
                print('Command not found!')