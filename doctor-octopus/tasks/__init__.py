from invoke import Collection

import aws
import generic

ns = Collection()
ns.add_task(aws.infra, 'get-infra')
ns.add_task(aws.configure, 'aws-configure')
# ns.add_collection(generic)

# tasks genéricas são adicionadas sequenciamente para facilitar chamadas
gmet = [method_name for method_name in dir(generic) if callable(getattr(generic, method_name))]
for g in gmet:
    if g != 'task':
        ns.add_task(getattr(generic, g), g)

