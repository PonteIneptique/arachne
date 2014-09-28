#!/usr/bin/python
# -*- coding: utf-8 -*-

class DataField:
	pass

class Field(DataField):
	def __init__(self, name, parameters = None, options = None):
		print name
		if isinstance(name, basestring) and not isinstance(name, unicode):
			name = unicode(name)
		if isinstance(name, unicode):
			self.name = name
		else:
			raise TypeError("Given name for the Field object is not a string")
		if len(name) == 0:
			raise ValueError("Field name is invalid")

		if options and not isinstance(options, basestring):
			raise TypeError("Options is not a basestring")

		if parameters and not isinstance(parameters, dict):
			raise TypeError("parameter is not a basestring")

		self.options = options
		self.parameters = parameters

class DataTable:
	pass

class Table(DataTable):
	def __init__(self, name, fields = [], keys = [], engine  = False, charset = False):

		self.fields = []
		self.name = ""
		self.keys = []
		self.engine = "InnoDB"
		self.charset = "utf8"

		if isinstance(name, basestring) and not isinstance(name, unicode):
			name = unicode(name)
		if isinstance(name, unicode):
			self.name = name
		else:
			raise TypeError("Given name for the Table object is not a string")

		if isinstance(engine, basestring):
			self.engine = engine
		if isinstance(charset, basestring):
			self.charset = charset

		if not isinstance(fields, list):
			raise TypeError("Given fields is not a list")
		if len(fields) > 0:
			self.setFields(fields)

	def setFields(self, fields = []):
		if not isinstance(fields, list):
			raise TypeError("Given fields is not a list")
		if len(fields) == 0:
			raise ValueError("Given list of fields is empty")

		for field in fields:
			self.addField(field)

	def addField(self,field):
		if field.name in [f.name for f in self.fields]:
			raise ValueError("A field with the name " + field.name + " already exists")
		self.fields.append(field)
