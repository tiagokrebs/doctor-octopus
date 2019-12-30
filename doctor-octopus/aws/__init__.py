from invoke import task
from .route53 import *


@task(name='configure')
def configure(c):
    """
    Efetua configuração do aws cli (obirgatótio)
    """
    print("Informe suas credenciais AWS")
    aws_configure()


@task(name='infra',
      help={'app': "App name (edg|app|foo)", 'env': "Canary(c), Dev(d), Prod(p), Stage(s)",
            'loc': "Airport (poa|mia|foo)", 'pop': "Datacenter (ovh|aws|foo)"})
def infra(c, app=None, env=None, loc=None, pop=None):
    """
    Obtém lista de servidores da zona .infra.azion.net
    """
    rsets = get_record_sets_names(app, env, loc, pop)
    for r in rsets:
        print(r)