import traceback
from fabric import task
from fabric import Connection
from ..aws.route53 import get_record_sets_names


@task(name='exec', help={'cmd': "Command to run", 'app': "Azion app name (edg|app|foo)",
                         'env': "Canary(c), Dev(d), Prod(p), Stage(s)", 'loc': "Airport (poa|mia|foo)",
                         'pop': "Datacenter (ovh|aws|foo)"})
def exec(c, cmd, app=None, env=None, loc=None, pop=None):
    """
    Run one line command on remote server
    """
    if 'host' in c:
        print('\n*** ' + c.host + ' ***')
        try:
            c.run("{}".format(cmd))
        except Exception as e:
            print(traceback.format_exc())
    else:
        if all(v is None for v in {app, env, loc, pop}):
            print('Expected one or combination of: --app|a, --env|-e, --loc|-l, --pop|-p, --host|-H')
            print('See octo --help exec')
        else:
            hosts = get_record_sets_names(app, env, loc, pop)
            for h in hosts:
                with Connection(host=h) as con:
                    print('\n*** ' + h + ' ***')
                    try:
                        con.run("{}".format(cmd))
                    except Exception as e:
                        print(traceback.format_exc())

