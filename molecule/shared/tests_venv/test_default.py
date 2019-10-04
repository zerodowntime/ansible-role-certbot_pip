import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
# def test_awscli_is_installed(host):
#     command = host.command('~/venv/certbot_pip/pip list')
#     assert command.stdout.find('certbot') > -1, "certbot is not installed"
# def test_named_data_runtime_dir_data(host):
#     with host.sudo():
#         file = host.file("~/venv/certbot_pip")
#         assert file.exists
#         assert file.is_directory
#         # assert file.mode == 0o770
#
#
# def test_certbot_is_installed(host):
#     command = host.command('~/venv/certbot_pip/bin/pip list')
#     assert command.stdout.find('certbot') > -1, "certbot not installed"
