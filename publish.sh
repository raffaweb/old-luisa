#!/bin/bash

now=$(date)
echo $now > .date
hg ci -m "Published on $now"
hg push
