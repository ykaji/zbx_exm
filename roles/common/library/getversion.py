#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, sys, shlex
from ansible.module_utils.basic import *

#--- Main Flow ---#
def main():
    rc = 1
    module = AnsibleModule(
        argument_spec = dict(
          specify = dict()
        )
    )

    specify_ver = module.params['specify']
    result = dict()

    if specify_ver:
        ver = specify_ver.split('.')
        rc = 0
 
    if specify_ver == '':
        module.exit_json(
            stdout  = "no version specification" ,
            changed = False ,
            rc      = rc
        )

    module.exit_json(
        version = ver[0] + "." + ver[1],
        changed = "True",
        rc      = 0
    )


if __name__ == '__main__':
    main()
