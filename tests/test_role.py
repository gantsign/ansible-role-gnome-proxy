import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_proxy_config_file(File):
    path = '/usr/share/glib-2.0/schemas/20_ansible-proxy.gschema.override'
    config_file = File(path)

    assert config_file.exists
    assert config_file.is_file
    assert config_file.user == 'root'
    assert config_file.group == 'root'
    assert oct(config_file.mode) == '0644'


@pytest.mark.parametrize('setting', [
    "mode='manual'",
    "autoconfig-url='http://pac.example.com'",
    r"ignore-hosts=\['localhost', '127.0.0.0/8', '::1'\]",
    "use-same-proxy=false",
    "host='http.example.com'",
    "port=3100",
    "use-authentication=true",
    "authentication-user='test_user'",
    "authentication-password='test_password'",
    "enabled=true",
    "host='https.example.com'",
    "port=3101",
    "host='ftp.example.com'",
    "port=3102",
    "host='socks.example.com'",
    "port=3103"
])
def test_proxy_config_contents(File, setting):
    path = '/usr/share/glib-2.0/schemas/20_ansible-proxy.gschema.override'
    config_file = File(path)

    assert config_file.exists
    assert config_file.is_file

    # File.contains uses grep
    assert config_file.contains(setting)