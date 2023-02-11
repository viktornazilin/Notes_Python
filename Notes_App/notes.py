from Model import file_operation
from Model import repository
from Controller import controller
from View import view


if __name__ == '__main__':
    file = file_operation.FileOperation('notes.csv')
    repo = repository.Repository(file)
    _controller = controller.Controller(repo)
    _view = view.View(_controller)
    _view.run()