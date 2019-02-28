#!/bin/sh

if [[ "$OSTYPE" == "darwin"* ]]; then

num_cores=`sysctl -n hw.ncpu`

else

num_cores=`nproc --all`

fi

echo $((num_cores + 1 )) gunicorns

gunicorn -w 3 \
-b 0.0.0.0:443 pixelBox:app \
--reload \
--log-level=DEBUG \
--pid=gunicorn.pid
