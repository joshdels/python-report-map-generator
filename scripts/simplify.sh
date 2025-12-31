#!/bin/bash

file_path="./data/flood"

# This scripts batch simplify the zip flood data

for i in "$file_path"/*.zip; do
  echo "Listing $i"
  unzip -l $i
done