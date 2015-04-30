#!/bin/bash

now=$(date)
echo $now > .date.txt
hg ci -m "Published on $now"
hg push
