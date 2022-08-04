
class Sql:

    def __init__(self) -> None:
        self.sql = ''

    def createsql(self, tipo, *args):
        sql = {
            'create': f'''CREATE TABLE {args[0]};''',
            'insert': {
                'user': f'''INSERT INTO user (cpf, nome, sobrenome) VALUES ('{args[1]}', '{args[2]}', '{args[3]}');''',
                'contas': f'''INSERT INTO contas (num, cpf, saldo) VALUES ('{args[1]}', '{args[2]}', '{args[3]}');'''},
            'update' : {
                'user' : f"UPDATE user SET {args[1]} = {args[2]} WHERE num = '{args[3]}';",
                'contas' : f"UPDATE contas SET {args[1]} = {args[2]} WHERE num = '{args[3]}';"
            },
            'read' : {
                'user' : f"SELECT * FROM user;",
                'contas' : f"SELECT * FROM contas;",
                'usercpf' : f"SELECT cpf FROM user WHERE cpf = {args[1]};"
            }
        }
        if tipo == 'create':
            self.sql = sql[tipo]
        else:
            self.sql = sql[tipo][args[0]]
