from invoke import Collection
import os

from . import aws
from . import generic

ns = Collection()
ns.add_task(aws.infra, 'get-infra')
ns.add_task(aws.configure, 'aws-configure')
# ns.add_collection(generic) #  método para adição de coleçōes

# tasks genéricas são adicionadas sequenciamente para facilitar chamadas
# ns.add_collection(generic)
gmet = [method_name for method_name in dir(generic) if callable(getattr(generic, method_name)) and method_name != 'Connection']
for g in gmet:
    if g != 'task':
        ns.add_task(getattr(generic, g), g)

# adiciona tarefas privadas em ./mytasks
print()
if os.path.exists(os.path.dirname(os.path.realpath(__file__)) + '/mytasks'):
    from . import mytasks
    ns.add_collection(mytasks, 'my')
