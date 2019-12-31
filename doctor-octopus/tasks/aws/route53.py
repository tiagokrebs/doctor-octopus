import os
import json
import re
from fabric import task


def get_record_sets_names(app=None, env=None, loc=None, pop=None):
    """
    Get ResourceRecordSets list of infra.azion.net zone on Route53
    :param app: Azion app hostname part
    :param env: dev|prod|canary|stage enviroment flag
    :param loc: global location (airport)
    :param pop: datacenter
    :return: list of recordsets names
    """
    rsets = os.popen("aws route53 list-resource-record-sets --hosted-zone-id Z3TGXCE6ZH10JR").read()
    jrsets = json.loads(rsets)
    names = [r['Name'][:-1] for r in jrsets['ResourceRecordSets']]

    # dynamic regex filter
    rstr = "%s-%s-%s(([0-9]{3}))%s\.infra\.azion\.net" % (app or '([a-z]{3})', loc or '([a-z]{3})', pop or '([a-z]{3})',
                                                         env or '[cdps]')
    r = re.compile(rstr)
    names = list(filter(r.match, names))
    return names


@task(name='infra', help={'app': "Azion app name (edg|app|foo)", 'env': "Canary(c), Dev(d), Prod(p), Stage(s)",
                          'loc': "Airport (poa|mia|foo)", 'pop': "Datacenter (ovh|aws|foo)"})
def infra(c, app=None, env=None, loc=None, pop=None):
    """
    Get server list from .infra.azion.net zone
    """
    rsets = get_record_sets_names(app, env, loc, pop)
    for r in rsets:
        print(r)
