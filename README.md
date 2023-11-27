
# Yuma Anugrah Virya Gunawan
**Development Environment** 
(27 November 2023)

## Simple Task
1. Buatlah image dari aplikasi sederhana yang sudah dibuat.
2. Jalankan image tersebut sebagai container dan berjalan pada port 8081
3. Berapakah IP docker container **whoami**?
4. Apa isi dari file yang tersembunyi dari docker container **whoami**? Clue: Volume Mounting
5. Image apa yang digunakan pada docker container **whoami**?

## Answer 1
### SSH into VM 

    ssh yumaanugrahviryagunawan@btj-academy.bangunindo.io

### Clone this repository

    git clone https://github.com/u1-byte/btj-academy.git

### Go inside repo directory

    cd btj-academy

### Build docker images from Dockerfile configuration

    docker build -t priotask:1.0.0 .

### Verify images created

    docker images

## Answer 2
### Run images as docker container on port 8081

    docker run -it -d -p 8081:8081 --name my-priotask priotask:1.0.0

### Verify container running

    docker ps

## Answer 3
### Inspect IP used by container whoami

    docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' whoami

### Output

> 172.17.0.2

## Answer 4
### Inspect container whoami mounts object

    docker inspect -f '{{json .Mounts}}' whoami

### Output

> [{ "Type":"bind", "Source":"/home/local/.docker",
> "Destination":"/tmp/system", "Mode":"", "RW":true,
> "Propagation":"rprivate" }]

    
### Go to whoami container and explore file inside destination directory

    docker exec -it whoami bin/sh
    ls tmp/system

### Output

> whoami

### Display content of whoami file

    cat tmp/system/whoami

### Output

> Oofooni1eeb9aengol3feekiph6fieve

## Answer 5
### Get image of container whoami

    docker inspect -f '{{.Config.Image}}' whoami

### Output

> secret:aequaix9De6dii1ay4HeeWai2obie6Ei
