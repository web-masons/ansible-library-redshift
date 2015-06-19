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

When in check-mode, for the purposes of testing, the following users will end up with the expected results:
  - test-redshift-user
    state=present
    password=abcD1234

  - missing-redshift-user
    state=absent
    password=hkyz7894


requirements: [ psycopg2 ]
author: Robert G. Johnson Jr.
'''

EXAMPLES = '''

'''

try:
    import psycopg2
except ImportError:
    psycopg2 = None

def connect(host_name, host_user, host_password, host_port, database):
    conn_string = "host='%s' user='%s' password='%s' port='%s' dbname='%s'" % (
        host_name, host_user, host_password, host_port, database
    )

    db_connection = psycopg2.connect(conn_string)
    return db_connection


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

    if not psycopg2:
        module.fail_json(msg="The python psycopg2 module is required to connect to Redshift")

    try:
        redshift = connect(module.params['host_name'],
                           module.params['host_user'],
                           module.params['host_password'],
                           module.params['host_port'],
                           module.params['host_database'])
        cursor = redshift.cursor()
    except Exception, e:
        module.fail_json(msg="Unable to connect to Redshift database: %s" % e)

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