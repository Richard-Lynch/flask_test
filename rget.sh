#!/bin/bash
command="79.97.206.77:8080/"
if [[ $# > 0 ]] ; then
    # echo "greater than 1"
    command="$command$1"
    # echo $command
fi
if [[ $# > 1 ]] ; then
    # echo "greater than 2"
    command="$command/$2"
    # echo $command
fi
if [[ $# > 2 ]] ;  then
    # echo "greater then 3"
    command="$command/$3"
    # echo $command
fi

echo $command
curl $command 
