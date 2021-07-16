
from generator import Generator


def main():
    instruction = Generator.generate_instruction('task37', 'dataJul-15-2021.json')
    # print(instruction)
    with open('script.sql', 'w') as script:
        script.write(instruction)


if __name__ == '__main__':
    main()
