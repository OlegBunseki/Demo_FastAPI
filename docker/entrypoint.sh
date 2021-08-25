#!/bin/bash

set -eou pipefail

if [ "$1" = "default" ]; then
    # do default things
    echo "Running with default settings"
    
    # exec conda run -n $PYTHONENV jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root --NotebookApp.token='' --NotebookApp.password=''    
    exec python ${PROJECT_FOLDER}/main.py
    # exec python src/test.py

else
    echo "Running user supplied args"
    # if the user supplied i.e. /bin/bash
    exec "$@"
    
fi