#!/usr/bin/env bash

case "$1" in
    producer1)
        docker \
            run \
                -it \
                --rm \
                --link $INFLUX_CONTAINER_NAME:influxdb \
                --net sandbox_default \
                --name producer1 \
            producer1
esac
