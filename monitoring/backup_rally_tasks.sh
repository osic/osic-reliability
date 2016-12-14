#!/bin/bash

$deployment=$1

mkdir -p task_results

rm -rf ./task_results/*

rm ./tasks.tar.gz

source /opt/rally/bin/activate

if [[ -n "$deployment" ]]; then
    `rally deployment use $1`
fi

for task in $(rally task list --uuids-only);do
    `rally task results $task > ./task_results/$task.json`
done

tar -czvf tasks.tar.gz ./task_results