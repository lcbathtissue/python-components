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
from src.main.python.programmingtheiot.data.SensorData import SensorData
from src.main.python.programmingtheiot.cda.sim.SensorDataGenerator import SensorDataSet

from src.main.python.programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask
from src.main.python.programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator

from src.main.python.programmingtheiot.data.SensorData import SensorData

class TemperatureSensorSimTask(BaseSensorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""
	DEFAULT_MIN_VAL = ConfigConst.DEFAULT_VAL
	DEFAULT_MAX_VAL = 100.0

	def __init__(self, name: str = ConfigConst.NOT_SET, typeID: int = ConfigConst.DEFAULT_SENSOR_TYPE,
				 dataSet: SensorDataSet = None, minVal: float = DEFAULT_MIN_VAL, maxVal: float = DEFAULT_MAX_VAL):
		super(TemperatureSensorSimTask, self).__init__(name = ConfigConst.TEMP_SENSOR_NAME,
													   typeID = ConfigConst.TEMP_SENSOR_TYPE,
													   dataSet = dataSet,
													   minVal = SensorDataGenerator.LOW_NORMAL_INDOOR_TEMP,
													   maxVal = SensorDataGenerator.HI_NORMAL_INDOOR_TEMP)
	