#!/bin/sh

network_name=production_flat-network

if [ -z $1 ]; then
  echo "Usage: $0 docker_image_name"
  exit 1
fi
image=$1

container_id_long=$(docker run -d -it $image)
if [ $? -ne 0 ]; then
  echo "docker run failed"
  exit 1
fi
container_id=$(echo $container_id_long | cut -c -12)

docker network connect --alias $container_id $network_name $container_id
curl http://localhost/container/switchover?dest=$container_id
curl http://localhost/
