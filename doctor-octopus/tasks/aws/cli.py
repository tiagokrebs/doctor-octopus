import os
from fabric import task


def aws_configure():
    """
    Start aws configuration
    :return: True
    """
    os.system('aws configure')
    return


@task(name='configure')
def configure(c):
    """
    Starts AWS Client configurarion (mandatory)
    """
    aws_configure()
