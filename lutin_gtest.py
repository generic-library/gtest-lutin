#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "gtest : google test interface"

def get_license():
	return "BSD 3 clauses"

def create(target):
	my_module = module.Module(__file__, 'gtest', 'LIBRARY_STATIC')
	my_module.add_src_file([
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
	my_module.add_header_file([
		'gtest/include/gtest/gtest-death-test.h',
		'gtest/include/gtest/gtest.h',
		'gtest/include/gtest/gtest-message.h',
		'gtest/include/gtest/gtest-param-test.h',
		'gtest/include/gtest/gtest_pred_impl.h',
		'gtest/include/gtest/gtest-printers.h',
		'gtest/include/gtest/gtest_prod.h',
		'gtest/include/gtest/gtest-spi.h',
		'gtest/include/gtest/gtest-test-part.h',
		'gtest/include/gtest/gtest-typed-test.h'
		], rm_path='gtest/include/')
	my_module.add_path(tools.get_current_path(__file__)+"/gtest")
	my_module.add_export_path(tools.get_current_path(__file__)+"/gtest/include/")
	return my_module



