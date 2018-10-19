#!/bin/bash

while true; do taskset -c 1 ./gpg-1.4.13 --yes -b echo.c; done
