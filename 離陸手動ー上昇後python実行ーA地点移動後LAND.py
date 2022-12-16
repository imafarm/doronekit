#!/usr/bin/env python
# -*- coding: utf-8 -*-
#座標指定モード 12/16

from dronekit import connect ,  VehicleMode ,LocationGlobalRelative
from pymavlink import mavutil # Needed for command message definitions

vehicle=connect('tcp:127.0.0.1:5762',wait_ready=True,timeout=60)

import time
import sys

vehicle.mode = VehicleMode("GUIDED")


#目標　緯度　軽度　高度 ;A地点
a_Location = LocationGlobalRelative(35.867003,140.305987,10)

#SIMPLE_GOtoを実行
vehicle.simple_goto(a_Location)
time.sleep(100)

vehicle.mode = VehicleMode("LAND")
