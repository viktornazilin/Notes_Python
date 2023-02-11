class Note:
    def __init__(self, id_note, title, msg, date_modified):
        self.__id_note = id_note
        self.__title = title
        self.__msg = msg
        self.__date_modified = date_modified

    def set_id(self, id_note):
        self.__id_note = id_note

    def get_id(self):
        return self.__id_note

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_msg(self, msg):
        self.__msg = msg

    def get_msg(self):
        return self.__msg

    def set_date(self, date_modified):
        self.__date_modified = date_modified

    def get_date(self):
        return self.__date_modified

    def __str__(self):
        return 'ID: ' + self.__id_note + '. Title: ' + self.__title + '. Message: ' + self.__msg + \
            '. Date modified: ' + self.__date_modified

    def __lt__(self, other):
        return self.__date_modified < other.get_date()