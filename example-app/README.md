## Simple Task - App Deployment
1. [Pada example python app, tambahkan beberapa routing kemudian custom port yang di listen.](https://github.com/u1-byte/btj-academy/tree/main/ansible#answer-1)
2. Buatlah satu playbook dengan beberapa task yaitu
- Menyalin file dari local ke server btj-academy
- Build docker image untuk example python app
- Jalankan container yang sudah dibuild
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
- Define one play named **Run docker container** with one task to run docker container.
- Use **ansible-yuma** as container name and **priotask** as image with tag value **1.0.0 (priotask:1.0.0)**, set interactive and tty value with true, and use port **8081:8081** 

### Execute Playbook

    ansible-playbook -i inventory.yaml playbook.yaml

### Verify container running

    docker ps