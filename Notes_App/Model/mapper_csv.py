from Model import note


class MapperCsv:
    def map_to_str(self, _note):
        if isinstance(_note, note.Note):
            return str(_note.get_id()) + ';' + _note.get_title() + ';' + _note.get_msg() + ';' + \
                _note.get_date()
        else:
            return 'Input data error!'

    def map_from_str(self, line):
        lines = line.split(';')
        if len(lines) == 4:
            return note.Note(lines[0], lines[1], lines[2], lines[3])
        else:
            print('Internal error!')