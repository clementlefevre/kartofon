#!/bin/bash

(sleep 30;amixer set Master 100%;/home/pi/berryconda3/bin/python /home/pi/workspace/kartofon/devtest.py &>>/home/pi/workspace/kartofon/kartofon.log)
