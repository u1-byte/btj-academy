## Simple Task - Ansible
1. [Buatlah sebuah inventory, pada inventory tersebut mendefinisikan daftar variables dan hosts](https://github.com/u1-byte/btj-academy/tree/main/ansible#answer-1)
2. [Buatlah satu playbook dengan task menjalankan sebuah docker container dengan kriteria yaitu terdapat image, port, dan environment variables](https://github.com/u1-byte/btj-academy/tree/main/ansible#answer-2)

## Answer 1
### Make sure ansible already available on VM

    ansible --version

### Make sure image that will be used already available

    docker images

### Create yaml file for inventory configuration
```yaml
all:
  vars:
    tag: 1.0.0
  hosts:
    btj-academy:
      ansible-host: 10.184.0.100
```
Define variable **tag** with value of image version
Define host **btj-academy** with ansible host IP value of VM host

## Answer 2
### Create yaml file for playbook configuration
```yaml
- name: Run docker container
  hosts: btj-academy
  become: true
  tasks:
    - docker_container:
        name: ansible-yuma
        image: "priotask:{{ tag }}"
        interactive: true
        tty: true
        ports:
          - "8081:8081"
```
Define one play named **Run docker container** with one task to run docker container.
Use **ansible-yuma** as container name and **priotask** as image with tag value **1.0.0 (priotask:1.0.0)**, set interactive and tty value with true, and use port **8081:8081** 
