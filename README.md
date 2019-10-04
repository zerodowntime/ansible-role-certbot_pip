# certbot_pip

Role to install Certbot package.

## Requirements

- Ansible >= 2.7

### Supported platforms

```yml
- EL
  - 7
- Ubuntu
  - xenial
```

## Default role variables

| Name | Description | Type | Default | Required |
| -----| ----------- | :--: | :------:| :------: |
| certbot__package_name | Package name to be installed | string | `certbot` | True |
| certbot__package_state | Whether to install the package or not | string | `present` | True |
| certbot__plugins | Certbot plugins to be installed. | list | `[]` | True |
| certbot__plugins_state | Wheter to install or remove certbot plugins. | string | `present` | True |
| certbot__virtualenv | Path to a virtualenv directory to install certbot into. | string | `None` | True |

**All default variables are described in [defaults/main.yml](defaults/main.yml) file.**



## Example Playbook

```yaml
    - hosts: all
      become: true
      roles:
        - role: zerodowntime.certbot_pip
```

## License

[Apache License 2.0](LICENSE)

## Support

ZeroDowntime Team <support@zdt.io>

For more information about the project, please visit <https://www.zdt.io/building-blocks/>.
