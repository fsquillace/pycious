#!/bin/bash
# script xepyhr-awesome
# author: dante4d <dante4d@gmail.com>
# author: Filippo Squillace <sqoox85@gmail.com>

RC_LUA=$1

if [ "$RC_LUA" == ""  ];
then
    RC_LUA="~/.config/awesome/rc.lua"
fi

Xephyr -ac -br -noreset -screen 800x600 :2 &
sleep 1


echo -e "awesome.restart()" | awesome-client

DISPLAY=:2.0 awesome -c $(readlink -f $RC_LUA)

