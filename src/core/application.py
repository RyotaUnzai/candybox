

class delegator(object):
    __view = None
    __model = None

    def __init__(self, view=None, model=None, *args, **kwargs):
        if view is not None:
            self.__view = view

        if model is not None:
            self.__model = model

    def connect(self):
        pass

    @property
    def view(self):
        return self.__view

    @view.setter
    def view(self, value):
        self.__view = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value
