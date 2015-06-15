#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "gtest : google test interface"

def get_license():
	return "BSD 3 clauses"

def create(target):
	myModule = module.Module(__file__, 'gtest', 'LIBRARY')
	myModule.add_src_file([
		'gtest/src/gtest-all.cc',
		'gtest/src/gtest.cc',
		'gtest/src/gtest-death-test.cc',
		'gtest/src/gtest-filepath.cc',
		'gtest/src/gtest_main.cc',
		'gtest/src/gtest-port.cc',
		'gtest/src/gtest-printers.cc',
		'gtest/src/gtest-test-part.cc',
		'gtest/src/gtest-typed-test.cc'
		])
	myModule.add_path(tools.get_current_path(__file__)+"/gtest")
	myModule.add_export_path(tools.get_current_path(__file__)+"/gtest/include/")
	return myModule



