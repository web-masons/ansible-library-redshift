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


def main():
    module = AnsibleModule(
        argument_spec=dict(
            user=dict(required=True),

            # Flags
            state=dict(default="present", choices=["absent", "present"]),
            allow_user_delete_fail=dict(type='bool', default='no')
        ),
        supports_check_mode=True
    )

    changed = False

    module.exit_json(changed=changed, user=module.params['user'])


# Pseudo-import the AnsibleModule helper class
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()