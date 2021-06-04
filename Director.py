class Director:
    def __init__(self):
        # Список строителей, управляемых директором.
        self.builder_list = []

    def add_builder(self, builder):
        self.builder_list.append(builder)

    def make_product(self):
        if not self.builder_list:
            print('There is no builders, it seems today is a holiday.')
        else:
            for builder in self.builder_list:
                # Каждый строитель в списке выполняет фиксированную последовательность действий.
                builder.create_pasta()
                builder.prepare_pasta()
                builder.add_sauce()
                builder.add_filling()
                builder.add_additive()
                pasta = builder.get_pasta()
                print(str(pasta))
