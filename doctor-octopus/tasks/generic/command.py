from fabric import task
from fabric import Connection


@task(name='exec', help={'cmd': "Comando a ser executado"})
def exec(c, cmd):
    """
    Executa comando em servidor(es)
    """
    host = ('app-orf-aws001s.infra.azion.net','app-orf-aws001s.infra.azion.net')
    for h in host:
        with Connection(host=h) as con:
            print('*** ' + h + ' ***')
            con.run("{}".format(cmd))
