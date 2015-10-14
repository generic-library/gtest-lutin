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
		'gtest/include/gtest/gtest-typed-test.h',
		'gtest/include/gtest/gtest-param-test.h',
		'gtest/include/gtest/gtest-message.h',
		'gtest/include/gtest/gtest-test-part.h',
		'gtest/include/gtest/gtest.h',
		'gtest/include/gtest/gtest-param-test.h.pump',
		'gtest/include/gtest/gtest-printers.h',
		'gtest/include/gtest/gtest-death-test.h',
		'gtest/include/gtest/gtest_pred_impl.h',
		'gtest/include/gtest/gtest_prod.h',
		'gtest/include/gtest/gtest-spi.h'
		], destination_path='gtest')
	my_module.add_header_file([
		'gtest/include/gtest/internal/gtest-param-util-generated.h.pump',
		'gtest/include/gtest/internal/gtest-type-util.h',
		'gtest/include/gtest/internal/gtest-tuple.h',
		'gtest/include/gtest/internal/gtest-param-util.h',
		'gtest/include/gtest/internal/gtest-string.h',
		'gtest/include/gtest/internal/gtest-linked_ptr.h',
		'gtest/include/gtest/internal/gtest-tuple.h.pump',
		'gtest/include/gtest/internal/gtest-param-util-generated.h',
		'gtest/include/gtest/internal/gtest-death-test-internal.h',
		'gtest/include/gtest/internal/gtest-port.h',
		'gtest/include/gtest/internal/gtest-type-util.h.pump',
		'gtest/include/gtest/internal/gtest-internal.h',
		'gtest/include/gtest/internal/gtest-filepath.h'
		], destination_path='gtest/internal')
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "gtest"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "gtest/include"))
	return my_module



