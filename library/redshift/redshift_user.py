#!/usr/bin/python

# (c) 2015, Robert G. Johnson Jr. <rjohnson@oakensoul.com>
#
#

DOCUMENTATION = '''
---
module: redshift_user
short_description: Create, Alter, Delete users in Amazon Redshift
description:
  - Create, Alter, Delete users in an Amazon Redshift cluster.
version_added: "0.1"

requirements: [ psycopg2 ]
author: Robert G. Johnson Jr.
'''

EXAMPLES = '''

'''

def check_if_system_state_would_be_changed():
    return False;


def main():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(default="present", choices=["absent", "present"]),
            user=dict(required=True),
            allow_user_delete_fail=dict(type='bool', default='no')
        ),

        supports_check_mode=True
    )

    changed = False

    if module.check_mode:
        # Check if any changes would be made but don't actually make those changes
        module.exit_json(changed=check_if_system_state_would_be_changed())

    module.exit_json(changed=changed, user=module.params['user'])
    # module.fail_json(msg="Something fatal happened")

# Pseudo-import the AnsibleModule helper class
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()