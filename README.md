Ansible Role: Gnome Proxy
=========================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-gnome-proxy.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-gnome-proxy)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.gnome--proxy-blue.svg)](https://galaxy.ansible.com/gantsign/gnome-proxy)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-gnome-proxy/master/LICENSE)

Role to configure the proxy settings for Gnome applications and other
applications that use the Gnome proxy settings (such as the Google Chrome web
browser).

Requirements
------------

* Ansible >= 2.4

    * Note: earlier versions of Ansible are likely to work but have not been
      tested.

* Linux Distribution

    * Debian Family

        * Ubuntu

            * Trusty (14.04)
            * Xenial (16.04)

    * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# The proxy mode (none, manual or auto)
gnome_proxy_mode:

# The URL of the proxy auto-config (PAC) file
# See: https://en.wikipedia.org/wiki/Proxy_auto-config
# https://en.wikipedia.org/wiki/Web_Proxy_Autodiscovery_Protocol
gnome_proxy_autoconfig_url:

# List of hostnames / IP addresses not to proxy
gnome_proxy_ignore_hosts:

# Use the specified proxy for all protocols
gnome_proxy_use_same_proxy:

# The hostname / IP address for the HTTP proxy
gnome_proxy_http_host:

# The port for the HTTP proxy
gnome_proxy_http_port:

# Whether the HTTP proxy requires authentication
gnome_proxy_http_use_authentication:

# The username used to access the HTTP proxy
gnome_proxy_http_authentication_user:

# The password used to access the HTTP proxy
gnome_proxy_http_authentication_password:

# Whether the HTTP proxy is enabled
gnome_proxy_http_enabled:

# The hostname / IP address for the HTTPS proxy
gnome_proxy_https_host:

# The port for the HTTPS proxy
gnome_proxy_https_port:

# The hostname / IP address for the FTP proxy
gnome_proxy_ftp_host:

# The port for the FTP proxy
gnome_proxy_ftp_port:

# The hostname / IP address for the SOCKS proxy
gnome_proxy_socks_host:

# The port for the SOCKS proxy
gnome_proxy_socks_port:

# Directory where GLib schemas are located
gnome_proxy_glib_schemas_directory: '/usr/share/glib-2.0/schemas'

# Name of override file for gnome_proxy config
gnome_proxy_overide_filename: '20_ansible-proxy.gschema.override'
```

Example Playbooks
-----------------

## Auto-proxy

```yaml
- hosts: servers
  roles:
    - role: gantsign.gnome-proxy
      gnome_proxy_mode: 'auto'
      # Gnome should be able to discover the auto-config URL using:
      # https://en.wikipedia.org/wiki/Web_Proxy_Autodiscovery_Protocol
      # if auto-discovery fails you can specify the URL as below:
      gnome_proxy_autoconfig_url: 'http://wpad.example.com/wpad.dat'
```

## Manual-proxy

```yaml
- hosts: servers
  roles:
    - role: gantsign.gnome-proxy
      gnome_proxy_mode: 'manual'
      gnome_proxy_ignore_hosts:
        - 'localhost'
        - '127.0.0.0/8'
        - '::1'
      gnome_proxy_use_same_proxy: yes
      gnome_proxy_http_host: 'proxy.example.com'
      gnome_proxy_http_port: 3128
      gnome_proxy_http_enabled: yes
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

To run the role (i.e. the `tests/test.yml` playbook), and test the results
(`tests/test_role.py`), execute the following command from the project root
(i.e. the directory with `molecule.yml` in it):

```bash
molecule test
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
