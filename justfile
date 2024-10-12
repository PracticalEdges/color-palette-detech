start:
    @echo "Starting streamlit on localhost:8501"
    docker run -p 8501:8501 -d color-detect

build:
    @echo "Building docker image"
    docker build -t color-detect .

clean:
    @echo "Stopping and removing any running containers using the color-detect image"
    docker ps -q --filter ancestor=color-detect | xargs -r docker stop
    docker ps -a -q --filter ancestor=color-detect | xargs -r docker rm
    @echo "Removing docker image"
    docker rmi color-detect