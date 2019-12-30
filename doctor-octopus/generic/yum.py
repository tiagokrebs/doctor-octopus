from invoke import task


@task(name='yum_install', help={'pkg': "Pacote a ser instalado"})
def yum_install(c, pkg):
    """
    Instala pacote com yum
    """
    print("executa yum install {}".format(pkg))


@task(name='yum_remove', help={'pkg': "Pacote a ser removido"})
def yum_remove(c, pkg):
    """
    Remove pacote com yum
    """
    print("executa yum remove {}".format(pkg))