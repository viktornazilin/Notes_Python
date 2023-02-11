class FileOperation:
    def __init__(self, filename):
        self.__filename = filename

    def read_all_lines(self):
        lines = []
        try:
            data = open(self.__filename, 'r')
            for line in data:
                lines.append(line.replace('\n', ''))
            data.close()
        except IOError:
            print('File read error!')
        return lines

    def save_all_lines(self, lines):
        try:
            with open(self.__filename, 'w') as data:
                for line in lines:
                    data.write(f'{line}\n')
        except IOError:
            print('File write error!')