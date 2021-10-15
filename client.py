class client():
    __name = "None";
    __cpf = 0;
    __rg = 0;
    __foto = False;

    def __init__(self):
        self.__name = "Nome"
        self.__cpf = 0;
        self.__rg = 0;
        self.__foto = False;

    def get_name(self):
        return self.__name;


    def get_cpf(self):
        return self.__cpf;


    def get_rg(self):
        return self.__rg;
    
    def get_foto(self):
        return self.__foto;