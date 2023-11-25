#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
#
import logging

from src.main.python.programmingtheiot.common.ResourceNameEnum import ResourceNameEnum

from src.main.python.programmingtheiot.data.ActuatorData import ActuatorData
from src.main.python.programmingtheiot.data.SensorData import SensorData
from src.main.python.programmingtheiot.data.SystemPerformanceData import SystemPerformanceData
from src.main.python.programmingtheiot.common.ITelemetryDataListener import ITelemetryDataListener
from src.main.python.programmingtheiot.common.ISystemPerformanceDataListener import ISystemPerformanceDataListener

class IDataMessageListener():
	"""
	Interface definition for data message listener clients.
	
	"""
	
	def getLatestActuatorDataResponseFromCache(self, name: str = None) -> ActuatorData:
		"""
		Retrieves the named actuator data (response) item from the internal data cache.
		
		@param name
		@return ActuatorData
		"""
		pass
		
	def getLatestSensorDataFromCache(self, name: str = None) -> SensorData:
		"""
		Retrieves the named sensor data item from the internal data cache.
		
		@param name
		@return SensorData
		"""
		pass
	
	def getLatestSystemPerformanceDataFromCache(self, name: str = None) -> SystemPerformanceData:
		"""
		Retrieves the named system performance data from the internal data cache.
		
		@param name
		@return SystemPerformanceData
		"""
		pass

	def handleActuatorCommandMessage(self, data: ActuatorData) -> ActuatorData:
		if data:
			logging.info("Processing actuator command message.")

			# TODO: add further validation before sending the command
			return self.actuatorAdapterMgr.sendActuatorCommand(data)
		else:
			logging.warning("Received invalid ActuatorData command message. Ignoring.")
			return None
	
	def handleActuatorCommandResponse(self, data: ActuatorData) -> bool:
		"""
		Callback function to handle an actuator command response packaged as a ActuatorData object.
		
		@param data The ActuatorData message received.
		@return bool True on success; False otherwise.
		"""
		pass
	
	def handleIncomingMessage(self, resourceEnum: ResourceNameEnum, msg: str) -> bool:
		"""
		Callback function to handle incoming messages on a given topic with
		a string-based payload.
		
		@param resourceEnum The topic enum associated with this message.
		@param msg The message received. It is expected to be in JSON format.
		@return bool True on success; False otherwise.
		"""
		pass

	def handleSensorMessage(self, data: SensorData) -> bool:
		"""
		Callback function to handle a sensor message packaged as a SensorData object.
		
		@param data The SensorData message received.
		@return bool True on success; False otherwise.
		"""
		pass
	
	def handleSystemPerformanceMessage(self, data: SystemPerformanceData) -> bool:
		"""
		Callback function to handle a system performance message packaged as
		SystemPerformanceData object.
		
		@param data The SystemPerformanceData message received.
		@return bool True on success; False otherwise.
		"""
		pass
	
	def setSystemPerformanceDataListener(self, listener: ISystemPerformanceDataListener = None):
		"""
		Sets the system performance listener. The listener's callback function will be invoked
		when system performance data is available.
		
		@param listener The listener reference.
		"""
		pass
	
	def setTelemetryDataListener(self, name: str = None, listener: ITelemetryDataListener = None):
		"""
		Sets the named telemetry data listener. The listener's callback function will be invoked
		when telemetry data is available for the given name.
		
		@param name The name of the listener.
		@param listener The listener reference.
		"""
		pass
	