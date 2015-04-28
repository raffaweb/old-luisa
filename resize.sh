#!/bin/bash

convert "$1" -resize "$2" -unsharp 2x0.5+0.7+0 -quality 98 "reduced-$1"
