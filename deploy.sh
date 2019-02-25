#!/bin/bash

docker-compose --file ./compose-files/docker-compose.yml down -v --remove-orphans
docker-compose --file ./compose-files/docker-compose.yml up -d --build --force-recreate
