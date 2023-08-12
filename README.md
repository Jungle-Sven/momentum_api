
1 build

sudo docker build -t momentum_api .

2 run

docker run -d --restart always -p 8083:8083 --name momentum_api_container --network momentum_network --log-opt mode=non-blocking --log-opt max-buffer-size=10m momentum_api

3 stop

sudo docker stop momentum_api_container

4 remove

sudo docker rm momentum_api_container

5 logs

sudo docker logs momentum_api_container
