from Builder import PastaBigoliBuilder, PastaTrofieBuilder, PastaOrecchietteBuilder
from Director import Director


def main():
    director = Director()

    bigoli_builder = PastaBigoliBuilder()
    trofie_builder = PastaTrofieBuilder()
    orecchiette_builder = PastaOrecchietteBuilder()

    director.add_builder(bigoli_builder)
    director.add_builder(trofie_builder)
    director.add_builder(orecchiette_builder)

    director.make_product()


if __name__ == '__main__':
    main()
