import json


class Generator:
    TOKENS = {'show_db': 'SHOW DATABASES', 'create_db': 'CREATE DATABASE', 'drop_db': 'DROP DATABASE',
              'use_db': 'USE', 'show_tables': 'SHOW TABLES', 'create_table': 'CREATE TABLE',
              '(': '(', ')': ')', 'int': 'INT', 'char': 'VARCHAR', 'null': 'NULL', 'auto_incr': 'AUTO_INCREMENT',
              'prime': 'PRIMARY KEY', 'not': 'NOT', ',': ',', ';': ';', 'inserto': 'INSERT INTO', 'values': 'VALUES', 'showculs': 'SHOW COLUMNS'}
    NAMES = {'clients': 'clients', 'id': 'id'}
    VALUES = {'char': '255'}
    TASKS = {'37': 'task37'}
    dic = {}
    buffer = ''

    @staticmethod
    def generate_instruction(task, json_file):
        instruction = ''

        with open(json_file, 'r') as jf:
            Generator.buffer = jf.read()
        cols = json.loads(Generator.buffer).get('cols')
        data = json.loads(Generator.buffer).get('data')
        print(data[0])

        # with open("file.txt", 'w') as f:
        #     f.write(d)

        values = ''
        table_rows = f"{Generator.NAMES.get('id')} {Generator.TOKENS.get('int')} {Generator.TOKENS.get('auto_incr')} {Generator.TOKENS.get('prime')}, "
        for col in cols:
            table_rows = f"{table_rows}{col} {Generator.TOKENS.get('char')}{Generator.TOKENS.get('(')}" \
                         f"{Generator.VALUES.get('char')}{Generator.TOKENS.get(')')}"
            table_rows = table_rows + ', '
            values = values + ', ' + f'{col}'
        table_rows = table_rows[:-2]
        values = values[2:]

        create_and_use = f"{Generator.TOKENS.get('create_db')} {Generator.NAMES.get('clients')}" \
                         f"{Generator.TOKENS.get(';')}\n{Generator.TOKENS.get('use_db')} {Generator.NAMES.get('clients')}" \
                         f"{Generator.TOKENS.get(';')}\n"

        data_name = 'data'
        create_table = f"{Generator.TOKENS.get('create_table')} {data_name}{Generator.TOKENS.get('(')}{table_rows}{Generator.TOKENS.get(')')}" \
                       f"{Generator.TOKENS.get(';')}\n"

        def insert_into(vals):
            insertion = f'{Generator.TOKENS.get("inserto")} {data_name} {Generator.TOKENS.get("(")}{values}{Generator.TOKENS.get(")")} ' \
                          f'{Generator.TOKENS.get("values")} {Generator.TOKENS.get("(")}{vals}{Generator.TOKENS.get(")")}{Generator.TOKENS.get(";")}\n'
            return insertion

        def insert_all():
            result = ''
            vals = ''
            ins = ''
            for elem in data:
                for line in elem:
                    vals = vals + ', ' + '"' + line + '"'
                vals = vals[2:]
                ins = insert_into(vals)
                vals = ''
                result = result + ins
            return result

        show_cols = f''


        if task == Generator.TASKS.get('37'):
            instruction = f'{create_and_use}{create_table}{insert_all()}'

        return instruction
