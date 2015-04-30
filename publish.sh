#!/bin/bash

now=$(date)
echo $date > .date
hg ci -m "Published on $now"
hg push
