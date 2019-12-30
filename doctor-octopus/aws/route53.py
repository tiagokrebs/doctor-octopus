import os
import json
import re


def get_record_sets_names(app=None, env=None, loc=None, pop=None):
    """
    Get ResourceRecordSets list of infra.azion.net zone on Route53
    :return: recordsets list of names
    """
    rsets = os.popen("aws route53 list-resource-record-sets --hosted-zone-id Z3TGXCE6ZH10JR").read()
    jrsets = json.loads(rsets)
    names = [r['Name'][:-1] for r in jrsets['ResourceRecordSets']]

    # ([a-z]{3})-([a-z]{3})-([a-z]{3})(([0-9]{3})[cdps])\.infra\.azion\.net
    rstr = "%s-%s-%s(([0-9]{3}))%s\.infra\.azion\.net" % (app or '([a-z]{3})', loc or '([a-z]{3})', pop or '([a-z]{3})',
                                                         env or '[cdps]')
    r = re.compile(rstr)
    names = list(filter(r.match, names))
    return names


def aws_configure():
    """
    Starts awscli configuration
    :return: True
    """
    os.system('aws configure')
    return


if __name__ == "__main__":
    aws_configure()
    print(get_record_sets_names('api'))
