set(CTEST_SOURCE_DIRECTORY "$ENV{GIRDER_SOURCE_DIR}")
set(CTEST_BINARY_DIRECTORY "$ENV{GIRDER_BUILD_DIR}")

include(${CTEST_SOURCE_DIRECTORY}/CTestConfig.cmake)
set(CTEST_SITE "Travis")
set(CTEST_BUILD_NAME "Linux-$ENV{TRAVIS_BRANCH}")
set(CTEST_CMAKE_GENERATOR "Unix Makefiles")
set(GAIA_MINERVA_COVERAGE_CONFIG "${CTEST_SOURCE_DIRECTORY}/plugins/gaia_minerva/plugin_tests/gaia_minerva.coveragerc")
set(test_group $ENV{GAIA_MINERVA_TEST_GROUP})
set(config_opts "")

list(APPEND config_opts
  "-DPYTHON_COVERAGE=$ENV{PY_COVG}"
  "-DPYTHON_VERSION=$ENV{TRAVIS_PYTHON_VERSION}"
  "-DSPARK_TEST_MASTER_URL=spark://localhost:7077"
  "-DPYTHON_COVERAGE_CONFIG=${GAIA_MINERVA_COVERAGE_CONFIG}"
  "-DCOVERAGE_MINIMUM_PASS=68"
  "-DJS_COVERAGE_MINIMUM_PASS=22"
)

ctest_start("Continuous")
ctest_configure(
  OPTIONS "${config_opts}"
)
ctest_build()

ctest_test(
  PARALLEL_LEVEL 1
  INCLUDE_LABEL "gaia_minerva_${test_group}"
  RETURN_VALUE res
)

if(test_group STREQUAL client)
  file(RENAME "${CTEST_BINARY_DIRECTORY}/js_coverage.xml" "${CTEST_BINARY_DIRECTORY}/coverage.xml")
endif()

ctest_coverage()
file(REMOVE "${CTEST_BINARY_DIRECTORY}/coverage.xml")
ctest_submit()

file(REMOVE "${CTEST_BINARY_DIRECTORY}/test_failed")
if(NOT res EQUAL 0)
  file(WRITE "${CTEST_BINARY_DIRECTORY}/test_failed" "error")
  message(FATAL_ERROR "Test failures occurred.")
endif()
