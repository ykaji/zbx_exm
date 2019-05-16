#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, sys, shlex
from ansible.module_utils.basic import *

verrevision='3.2.4'

#--- Main Flow ---#
def main():
    rc = 1
    zeropad = ''

    module = AnsibleModule(
        argument_spec = dict(
          verrevision = dict()
        )
    )

    workval = module.params['verrevision'].split('.')
    result = dict()

    if workval:
        for val in workval:
            zeropad += val.zfill(2)

        rc = 0
 
    if workval == '':
        module.exit_json(
            stdout  = "no Value" ,
            changed = False ,
            rc      = rc
        )

    module.exit_json(
        zeropad_version = zeropad ,
        changed = "True" ,
        rc      = 0
    )


if __name__ == '__main__':
    main()
