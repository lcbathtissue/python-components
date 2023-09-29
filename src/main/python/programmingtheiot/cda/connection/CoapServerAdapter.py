#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import logging

from threading import Thread
from time import sleep

from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource

import src.main.python.programmingtheiot.common.ConfigConst as ConfigConst

from src.main.python.programmingtheiot.common.ConfigUtil import ConfigUtil
from src.main.python.programmingtheiot.common.ResourceNameEnum import ResourceNameEnum

from src.main.python.programmingtheiot.common.IDataMessageListener import IDataMessageListener
from src.main.python.programmingtheiot.cda.connection.handlers.GetTelemetryResourceHandler import GetTelemetryResourceHandler
from src.main.python.programmingtheiot.cda.connection.handlers.UpdateActuatorResourceHandler import UpdateActuatorResourceHandler
from src.main.python.programmingtheiot.cda.connection.handlers.GetSystemPerformanceResourceHandler import GetSystemPerformanceResourceHandler

class CoapServerAdapter():
	"""
	Definition for a CoAP communications server, with embedded test functions.
	
	"""
	
	def __init__(self, dataMsgListener = None):
		pass
		
	def addResource(self, resourcePath: ResourceNameEnum = None, endName: str = None, resource = None):
		pass
				
	def startServer(self):
		pass
	
	def stopServer(self):
		pass
	
	def setDataMessageListener(self, listener: IDataMessageListener = None) -> bool:
		pass
