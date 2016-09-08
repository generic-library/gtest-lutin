#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os


def get_type():
	return "LIBRARY_STATIC"

def get_desc():
	return "google test interface"

def get_licence():
	return "BSD-3"

def get_compagny_type():
	return "com"

def get_compagny_name():
	return "Google"

def get_maintainer():
	return ["mailing-list gtest <googletestframework@googlegroups.com>"]

def get_version():
	return [1,7,0]

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
		'googletest/googletest/src/gtest-all.cc',
		'googletest/googletest/src/gtest.cc',
		'googletest/googletest/src/gtest-death-test.cc',
		'googletest/googletest/src/gtest-filepath.cc',
		'googletest/googletest/src/gtest_main.cc',
		'googletest/googletest/src/gtest-port.cc',
		'googletest/googletest/src/gtest-printers.cc',
		'googletest/googletest/src/gtest-test-part.cc',
		'googletest/googletest/src/gtest-typed-test.cc'
		])
	my_module.add_header_file([
		'googletest/googletest/include/gtest/gtest-typed-test.h',
		'googletest/googletest/include/gtest/gtest-param-test.h',
		'googletest/googletest/include/gtest/gtest-message.h',
		'googletest/googletest/include/gtest/gtest-test-part.h',
		'googletest/googletest/include/gtest/gtest.h',
		'googletest/googletest/include/gtest/gtest-param-test.h.pump',
		'googletest/googletest/include/gtest/gtest-printers.h',
		'googletest/googletest/include/gtest/gtest-death-test.h',
		'googletest/googletest/include/gtest/gtest_pred_impl.h',
		'googletest/googletest/include/gtest/gtest_prod.h',
		'googletest/googletest/include/gtest/gtest-spi.h'
		], destination_path='gtest')
	my_module.add_header_file([
		'googletest/googletest/include/gtest/internal/gtest-internal.h',
		'googletest/googletest/include/gtest/internal/gtest-param-util-generated.h.pump',
		'googletest/googletest/include/gtest/internal/gtest-port.h',
		'googletest/googletest/include/gtest/internal/gtest-tuple.h.pump',
		'googletest/googletest/include/gtest/internal/gtest-death-test-internal.h',
		'googletest/googletest/include/gtest/internal/gtest-linked_ptr.h',
		'googletest/googletest/include/gtest/internal/gtest-param-util.h',
		'googletest/googletest/include/gtest/internal/gtest-string.h',
		'googletest/googletest/include/gtest/internal/gtest-type-util.h',
		'googletest/googletest/include/gtest/internal/gtest-filepath.h',
		'googletest/googletest/include/gtest/internal/gtest-param-util-generated.h',
		'googletest/googletest/include/gtest/internal/gtest-port-arch.h',
		'googletest/googletest/include/gtest/internal/gtest-tuple.h',
		'googletest/googletest/include/gtest/internal/gtest-type-util.h.pump'
		], destination_path='gtest/internal')
	my_module.add_header_file([
		'googletest/googletest/include/gtest/internal/custom/gtest-port.h',
		'googletest/googletest/include/gtest/internal/custom/gtest-printers.h',
		'googletest/googletest/include/gtest/internal/custom/gtest.h'
		], destination_path='gtest/internal/custom/')
	my_module.add_depend([
	    'cxx',
	    'm',
	    'pthread',
	    'arpa',
	    'rpc'
	    ])
	
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "googletest/googletest"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "googletest/googletest/include"))
	return my_module



