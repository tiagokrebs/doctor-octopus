import os
from fabric import task


def aws_configure():
    """
    Starts awscli configuration
    :return: True
    """
    os.system('aws configure')
    return


@task(name='configure')
def configure(c):
    """
    Efetua configuração do aws cli (obirgatótio)
    """
    print("Informe suas credenciais AWS")
    aws_configure()