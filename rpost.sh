#!/bin/bash

V1=$1
V2=$2
V3=$3

json_template='{
    name: $v1,
    pros: $v2,
    cons: $v3
}'
address="http://79.97.206.77:8080"
jq -n --arg v1 "$V1" \
    --arg v2 "$V2" \
    --arg v3 "$V3" "$json_template" |
    curl -sS -X POST \
    -H "Content-Type: application/json" \
    -d@- \
    "$address"/langs
