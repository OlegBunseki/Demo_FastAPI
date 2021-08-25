FROM ubuntu:20.04

# Declare some ARGument and ENVironemnt variables
ARG CONDA_VERSION=4.9.2
ARG CONDA_DIR=/opt/conda

ARG PYTHON_VERSION=37
ARG PYTHONENV=aiservice

ENV PROJECT_FOLDER=app
ENV PYTHONFAULTHANDLER=1
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Installation of some libraries / RUN some commands on the base image
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y \
        wget \
        git \
        bzip2 \
        libopenblas-dev \
        pbzip2 \
        libgl1-mesa-glx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Don’t run Docker as root
RUN useradd --create-home appuser

### Install Anaconda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-py${PYTHON_VERSION}_${CONDA_VERSION}-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    /bin/bash /tmp/miniconda.sh -b -p $CONDA_DIR && \
    rm -rf /tmp/* && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PATH $CONDA_DIR/bin:$PATH

### Install Environment
# Be sure to only copy the file environment.yml before to copy the full current directory. 
# Otherwise any change in the directory would invalidate the docker cache. 
# We only want to re-create the conda environment if environment.yml changes.
COPY docker/env.yml ${PROJECT_FOLDER}/docker/env.yml

RUN conda env create -n ${PYTHONENV} -f ${PROJECT_FOLDER}/docker/env.yml && \
    rm -rf /opt/conda/pkgs/* && \
    echo "source activate ${PYTHONENV}" > ~/.bashrc

ENV PATH /opt/conda/envs/${PYTHONENV}/bin:$PATH

### Copy Project to Docker
COPY . ${PROJECT_FOLDER}

### Make Etrypoint execetubale
RUN chmod +x ${PROJECT_FOLDER}/docker/entrypoint.sh


### Start Image

# Option 1:
# CMD [ "/bin/bash" ]

# Option 2:
# ENTRYPOINT [ "app/docker/entrypoint.sh" ]
# CMD [ "default" ]

# Option 3:
ENTRYPOINT [ "/bin/bash", "-c", "${PROJECT_FOLDER}/docker/entrypoint.sh ${@}", "--" ]
CMD [ "default" ]