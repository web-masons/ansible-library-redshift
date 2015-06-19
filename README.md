# Ansible Role: Redshift
[![Build Status](https://secure.travis-ci.org/oakensoul/ansible-role-redshift.png)](http://travis-ci.org/oakensoul/ansible-role-redshift)

This project creates a handful of libraries for managing Redshift users using Ansible similar to the PostgreSQL modules
in Ansible.

I'll apologize now as this is my first venture into creating Ansible modules. Feedback, Issues, and pull requests are
more than welcome.


## Thank  You
I wanted to add a thank you to the Ansible community for providing many examples of standards to build off of. I also
specifically want to call out / thank [geerlingguy](http://github.com/geerlingguy) as I use a number of his roles from
Ansible Galaxy and I've been reading and learning a lot from his roles on Github.

## Requirements

psycopg2 is required.

## Role Variables

A description of the settable variables for this role should go here, including any variables that are in
defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables
that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

## Dependencies

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set
for other roles, or variables that are used from other roles.

## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for
users too:

    - hosts: redshift
      roles:
         - { role: username.rolename, x: 42 }

```bash
$ cd \vagrant
$ ansible-playbook tests/test.yml --inventory=tests/inventory --connection=local -M library/redshift/
```

# License

(c) 2015, Robert G. Johnson Jr. <rjohnson@oakensoul.com>, Apache Version 2.0

## Author Information

This role was created in 2015 by [Robert G. Johnson Jr.](http://github.com/oakensoul).
