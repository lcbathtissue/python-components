#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import src.main.python.programmingtheiot.common.ConfigConst as ConfigConst

from src.main.python.programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask
from src.main.python.programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator
from src.main.python.programmingtheiot.data.SensorData import SensorData



class HumiditySensorSimTask(BaseSensorSimTask):
	def __init__(self, dataSet = None):
		super( \
			HumiditySensorSimTask, self).__init__( \
				name = ConfigConst.HUMIDITY_SENSOR_NAME, \
				typeID = ConfigConst.HUMIDITY_SENSOR_TYPE, \
				dataSet = dataSet, \
				minVal = SensorDataGenerator.LOW_NORMAL_ENV_HUMIDITY, \
				maxVal = SensorDataGenerator.HI_NORMAL_ENV_HUMIDITY)
	