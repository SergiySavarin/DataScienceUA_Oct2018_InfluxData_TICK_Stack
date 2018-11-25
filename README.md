
[Install](#Install)  [Google Form](https://l.facebook.com/l.php?u=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSdx-MFpdefBevuZV-bNsk-xX_SMqrSyatVf5u0w_FWQvb3Org%2Fviewform%3Ffbclid%3DIwAR3STIYPv7eXRMsiAOWW6HEsb4s1qeUsfqOU5MEa9mFkUTsKBzx3Bi-NWvw&h=AT0PtuNUkKaFTHzH5RdXVUmYueG9iBH85PVMeX8Ec1Fzlfkzj0g-_QZYyYVQyGTIlsceDWDT7z6F4J0ojYikoPTmZwjG9x1vT3h-rDxW-w_czdarR_tID3WVtdRldA)  [Workshop Slides](https://www.slideshare.net/sergiysavarin/influx-data-basic)

# Project description

Basic of using InfluxData stack.

First of all install the project and run `sandbox` and `producer1`.

Then, when data will start comming to `raw_trade_data` database
create new Kapacitor tasts:

1. enter [Kapacitor](http://localhost:8888/sources/10000/alert-rules)
2. created new batch task.
3. copy `src/producer/batch` script text to new created batch task.
4. Save and enable batch task.
3. use tha same steps to create stream task with script text from `src/producer/stream`


# Install

Install [Docker](https://www.docker.com/get-started) and
[Docker Compose](https://docs.docker.com/compose/install/) for Mac/Linux/Windows

```bash
# Run sandbox
git clone git@github.com:SergiySavarin/DataScienceUA_Oct2018_InfluxData_TICK_Stack.git
cd DataScienceUA_Oct2018_InfluxData_TICK_Stack/src/sandbox
./sandbox up

# Create influx database for producer
./sandbox influxdb cli
Using latest, stable releases
Entering the influx cli...
Connected to http://localhost:8086 version 1.7.1
InfluxDB shell version: 1.7.1
Enter an InfluxQL query
> CREATE DATABASE raw_trade_data

# Set influcontainer name variable
export INFLUX_CONTAINER_NAME=$(docker-compose ps | grep sandbox_influxdb | awk '{print $1}')

# Build docker for producer
cd ../producer
docker build -f Dockerfile.p1 -t producer1 .

# Run producer1
./run.sh producer1
```

# Knowledge level required

    - Python (basic)
    - SQL (basic)
    - Docker (basic)

# Good to review

## InfluxData TICK stack
https://www.influxdata.com/university/ (Getting Started Series)

https://docs.influxdata.com/influxdb/v1.7/concepts/key_concepts/

https://docs.influxdata.com/kapacitor/v1.5/tick/introduction/

https://www.influxdata.com/resources/watch-everything-watch-anything-anomaly-detection-by-nathaniel-cook/

https://www.influxdata.com/training/7-intro-kapacitor-alerting-anomaly-detection/

https://www.influxdata.com/resources/structured-logging/

## Streams in general
http://infolab.stanford.edu/~ullman/mmds/ch4.pdf

https://medium.com/stream-processing/what-is-stream-processing-1eadfca11b97

https://wso2.com/library/articles/2018/02/stream-processing-101-from-sql-to-streaming-sql-in-ten-minutes/
