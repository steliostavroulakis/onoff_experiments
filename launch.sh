# Classical Docker
docker run --entrypoint /bin/bash -v $(pwd):/app -p 6000:6000 -e DISPLAY=localhost:0 --rm -i -t onoff

# Jupyterlab Interactive
#docker run -p 8888:8888 -e DISPLAY=localhost:0 -e JUPYTER_ENABLE_LAB=yes -e JUPYTER_TOCKEN=docker infact
#docker run -p 8888:8888 -e DISPLAY=localhost:0 -e JUPYTER_ENABLE_LAB=yes -e JUPYTER_TOKEN=docker onoff
#docker run -p 8888:8888 -e DISPLAY=localhost:0 -e JUPYTER_ENABLE_LAB=yes onoff