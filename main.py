import json


def read_data(json_file):
    with open(json_file, 'r') as jf:
        return json.load(jf)


def generate_text(data):
    text = f"use storage\ndb.createCollection('products')\n" \
           f"db.products.insertMany({data})\n"
    return text


def main():
    with open('script.txt', 'w') as script:
        script.write(generate_text(read_data("MOCK_DATA.json")))


if __name__ == '__main__':
    main()
