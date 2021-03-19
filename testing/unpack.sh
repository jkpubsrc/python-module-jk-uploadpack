#!/bin/bash


rm -rf foo
mkdir foo
cd foo
cat ../pack.up | tar -x
jsonPrettyPrint.py meta.json > meta-pretty.json


