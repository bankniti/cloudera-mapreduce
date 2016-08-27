# Docker cloudera/quickstart with mapReduce testing

Getting up and running
----------------------

## Requirements

- [Docker](https://www.docker.com/)


## Build Dockerfile

- Go to folder where Dockerfile located
- `docker build -t [image_name] .`


Deployment
------------

Run these commands in where Dockerfile located:
- `docker run --hostname=quickstart.cloudera --privileged=true -it --rm -v $PWD:/usr/home/mapreduce [image_name] /usr/bin/docker-quickstart`

Run mapReduce test
--------------------

- `cat test.txt | ./map.py | sort | ./reduce.py`


Reference
------------
- https://hub.docker.com/r/cloudera/quickstart/
