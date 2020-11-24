# class
class amigo():
    # cnstr
    def __init__(self, amistad_id, id_user_1, id_user_2):
        self.__amistad_id = amistad_id
        self.__id_user_1 = id_user_1
        self.__id_user_2 = id_user_2
    # mtds
    # gtt
    def get_amistad_id(self):
        return self.__amistad_id
    def get_id_user_1(self):
        return self.__id_user_1
    def get_id_user_2(self):
        return self.__id_user_2
    # stt
    def set_amistad_id(self, nw_amistad_id):
        self.__amistad_id = nw_amistad_id
    def set_id_user_1(self, nw_id_user_1):
        self.__id_user_1 = nw_id_user_1
    def set_id_user_2(self, nw_id_user_2):
        self.__id_user_2 = nw_id_user_2