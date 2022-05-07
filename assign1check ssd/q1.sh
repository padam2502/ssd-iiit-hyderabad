#!/bin/bash
du -h -d 1 | sort -hr | awk 'BEGIN {FS="./"} NR!=1 {print $2"\t"$1;}'
