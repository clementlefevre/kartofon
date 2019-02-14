#!/bin/bash

(sleep 30;amixer set Master 100%;/usr/bin/python /home/pi/kartofon/devtest.py &>>/home/pi/kartofon/kartofon.log)
