from abc import ABC, abstractmethod

from pasta import Pasta


class Builder(ABC):

    name = ''
    pasta = 0

    @abstractmethod
    def prepare_pasta(self, pasta):
        pass

    @abstractmethod
    def add_sauce(self, pasta):
        pass

    @abstractmethod
    def add_filling(self, pasta):
        pass

    @abstractmethod
    def add_additive(self, pasta):
        pass


class PastaBigoliBuilder(Builder):

    def __init__(self):
        self.name = 'Pasta Bigoli Builder'

    def create_pasta(self):
        self.pasta = Pasta('Bigoli')

    def prepare_pasta(self):
        self.pasta.set_pasta('bigoli')

    def add_sauce(self):
        self.pasta.set_sauce('marinara')

    def add_filling(self):
        self.pasta.set_filling('chicken')

    def add_additive(self):
        self.pasta.set_additive('cheese')

    def get_pasta(self):
        return self.pasta


class PastaTrofieBuilder(Builder):

    def __init__(self):
        self.name = 'Pasta Trofie Builder'

    def create_pasta(self):
        self.pasta = Pasta('Trofie')

    def prepare_pasta(self):
        self.pasta.set_pasta('trofie')

    def add_sauce(self):
        self.pasta.set_sauce('pesto')

    def add_filling(self):
        self.pasta.set_filling('sausage')

    def add_additive(self):
        self.pasta.set_additive('vegetables')

    def get_pasta(self):
        return self.pasta


class PastaOrecchietteBuilder(Builder):

    def __init__(self):
        self.name = 'Pasta Orecchiette Builder'

    def create_pasta(self):
        self.pasta = Pasta('Orecchiette')

    def prepare_pasta(self):
        self.pasta.set_pasta('orecchiette')

    def add_sauce(self):
        self.pasta.set_sauce('alfredo')

    def add_filling(self):
        self.pasta.set_filling('mushroom')

    def add_additive(self):
        self.pasta.set_additive('olives')

    def get_pasta(self):
        return self.pasta
