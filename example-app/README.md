## Simple Task - App Deployment

1. [Pada example python app, tambahkan beberapa routing kemudian custom port yang di listen.](https://github.com/u1-byte/btj-academy/tree/main/example-app#answer-1)

2. Buatlah satu playbook dengan beberapa task yaitu : 
- [Menyalin file dari local ke server btj-academy](https://github.com/u1-byte/btj-academy/tree/main/example-app#copy-file-to-another-directory)
- [Build docker image untuk example python app](https://github.com/u1-byte/btj-academy/tree/main/example-app#build-docker-image)
- [Jalankan container yang sudah dibuild](https://github.com/u1-byte/btj-academy/tree/main/example-app#run-docker-container)

### Note
Example python app from this repo https://github.com/rrw-bangunindo/btj-academy

## Answer 1
### Edit app.py file
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/not-hello')
def not_hello():
    return 'Hi, Docker!'

@app.route('/good-bye')
def good_bye():
    return 'Bye, Docker!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5005)
```

 - Adding some route like **/not-hello** and **/good-bye**. Route **/not-hello** will display **Hi, Docker!** and route **/good-bye** will display **Bye, Docker!**
 - Set app port into port **5005**

## Answer 2
### Create Dockerfile configuration
```dockerfile
FROM python:3.9-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
``` 

### Create yaml file for inventory configuration
```yaml
all:
  vars:
    image: i-flask-yuma
    tag: 1.0.0
    source: ../example-app/
    destination: btj-academy/destination-dir/
    container_name: c-flask-yuma
    port: 5005:5005
  hosts:
    btj-academy:
      ansible-host: 10.184.0.100
```

 - All variable will be used on **playbook.yaml**
 - Make sure port value same as app (**port 5005**)
 - Source and destination value explained [here](https://github.com/u1-byte/btj-academy/tree/main/example-app#copy-file-to-another-directory)

### Create yaml file for playbook configuration
```yaml
 - name: Run multiple task
  hosts: btj-academy
  become: true
  tasks:
    - name: Copy file to another directory
      ansible.builtin.copy:
        src: "{{ source }}"
        dest: "{{ destination }}"
    - name: Build docker image
      community.docker.docker_image:
        name: "{{ image }}"
        tag: "{{ tag }}"
        build:
          path: "{{ destination }}"
        source: "build"        
    - name: Run docker container
      docker_container:
        name: "{{ container_name }}"
        image: "{{ image }}:{{ tag }}"
        interactive: true
        tty: true
        ports:
          - "{{ port }}"
```
 - Set one 'play' with multiple tasks : **Copy file to another directory, Build docker image, and Run docker container**

### Copy file to another directory
 - Set current directory (**example-app**) as **source** value to get all the file in this directory
 - Set **btj-academy/destination-dir** as **destination** value to paste all file into new directory on VM named **destination-dir**. (**Note:** I use server to server with different directory to simulate copy file from local to server because my local docker not working).
 - Use source (src) and destination (dest) value from inventory

### Build docker image
- Use image, tag and destination value from inventory
- Set **source** value into **build** because we want to build the image from Dockerfile on the destination path.

### Run docker container
 - Use container_name, image, tag, and port value from inventory
 - Image used will be **i-flask-yuma:1.0.0**
 - Container created will be **c-flask-yuma**
 - Port used will be **5005:5005**  

### Execute Playbook

    ansible-playbook -i inventory.yaml playbook.yaml

### Verify file copied from source directory into destination directory

    ls ../destination-dir

### Verify docker image created

    docker images | grep i-flask-yuma

### Verify container running

    docker ps | grep c-flask-yuma

### Verify all route accessable
Open in browser :
 - http://btj-academy.bangunindo.io:5005/ (Output : Hello, Docker!)
 - http://btj-academy.bangunindo.io:5005/not-hello (Output : Hi, Docker!)
 - http://btj-academy.bangunindo.io:5005/good-bye (Output : Bye, Docker!)

### Check container logs

    docker logs c-flask-yuma
