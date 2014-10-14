#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# code by elaiyan (Laiyuan yang)

import os
import xml.dom.minidom
import string
import time
import sys

class TestCases(object):
	"""docstring for TestCases"""
	def __init__(self, xmlfile):
		super(TestCases, self).__init__()
		self.xmlfile = xmlfile
		dom = xml.dom.minidom.parse(xmlfile)
		self.root = dom.documentElement
		self.product = {}
		self.script  = []
		self.__initData()

	def __initData(self):
		root = self.root
		for node in root.childNodes:
			if node.nodeName == "testcase":
				for tcSubNode in node.childNodes:
					# parser path 
					if tcSubNode.nodeName == "path":
						if tcSubNode.firstChild.data not in self.script:
							self.script.append(tcSubNode.firstChild.data)
					# parser product-type
					if tcSubNode.nodeName == "supports":
						for spSubNode in tcSubNode.childNodes:
							if spSubNode.nodeName == "testobjects":
								for toSubNode in spSubNode.childNodes:
									if  toSubNode.nodeName == "product-type":
										key = toSubNode.firstChild.data
										if self.product.has_key(key):
											self.product[key] = self.product[key] + 1
										else:
											self.product[key] = 1
										
	def getAllProductType(self):
		return self.product

	def getAllScript(self):
		return self.script
	def filterByProductType(self, productType):
		if productType not in self.product.keys():
			print "please choice a exit product"
			return 
		root = self.root
		scripts = []

		for node in root.childNodes:
			if node.nodeName == "testcase":
				for tcSubNode in node.childNodes:
					# parser path 
					if tcSubNode.nodeName == "path":
						if tcSubNode.firstChild.data not in scripts:
							currentScript = tcSubNode.firstChild.data
						else:
							break
					# parser product-type
					if tcSubNode.nodeName == "supports":
						for spSubNode in tcSubNode.childNodes:
							if spSubNode.nodeName == "testobjects":
								for toSubNode in spSubNode.childNodes:
									if  toSubNode.nodeName == "product-type":
										key = toSubNode.firstChild.data
										if key == productType:
											scripts.append(currentScript)
		return scripts
	def filterByProductTypeAndScript(self, productType, scriptName):
		if productType not in self.product.keys():
			print "please choice a exit product"
			return 

		root = self.root
		scripts = []

		for node in root.childNodes:
			if node.nodeName == "testcase":
				for tcSubNode in node.childNodes:
					# parser path 
					if tcSubNode.nodeName == "path":
						if tcSubNode.firstChild.data not in scripts:
							currentScript = tcSubNode.firstChild.data
						else:
							break
					# parser product-type
					if tcSubNode.nodeName == "supports":
						for spSubNode in tcSubNode.childNodes:
							if spSubNode.nodeName == "testobjects":
								for toSubNode in spSubNode.childNodes:
									if  toSubNode.nodeName == "product-type":
										key = toSubNode.firstChild.data
										if key == productType:
											scripts.append(currentScript)

def main():
	xmlfile = "C:\\sw\\terass\\msr\\parameters\\rul\\common\\testcases.xml"
	tcs = TestCases(xmlfile)
	# products = tcs.getAllProductType()
	# for (product, times) in products.items():
	# 	print "products: " + product + " times: " + str(times)

	# for script in tcs.script:
	# 	print script
	productType = "rrug12_b31800%2"
	print "script for rrug12_b31800%2. total is " + str(tcs.getAllProductType()[productType])
	
	
	for script in tcs.filterByProductType(productType):
		print script

if __name__ == '__main__':
	main()

		 



