from invoke import task


@task(name='ls', help={'dir': "Diretório a ser listado"})
def ls(c, dir):
    """
    Lista conteúdo de um diretório
    """
    c.run("ls {}".format(dir))