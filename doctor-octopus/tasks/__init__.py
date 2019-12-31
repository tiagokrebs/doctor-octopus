from invoke import Collection
import os

from . import aws
from . import generic

ns = Collection()
ns.add_task(aws.infra, 'get-infra')
ns.add_task(aws.configure, 'aws-configure')
ns.add_task(generic.exec, 'exec')

# add colection of private tasks from ./mytasks (my.*)
print()
if os.path.exists(os.path.dirname(os.path.realpath(__file__)) + '/mytasks'):
    from . import mytasks
    ns.add_collection(mytasks, 'my')
