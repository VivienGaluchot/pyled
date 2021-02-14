#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "Usage: set [red] [green] [blue]"
    exit 1
fi

pigs p 17 $1
pigs p 22 $2
pigs p 27 $3