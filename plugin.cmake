get_filename_component(PLUGIN ${CMAKE_CURRENT_LIST_DIR} NAME)
add_eslint_test(${PLUGIN} "${PROJECT_SOURCE_DIR}/plugins/${PLUGIN}/web_client/
add_python_test(geoprocess PLUGIN gaia_minerva)
add_python_test(geoservice_proxy PLUGIN gaia_minerva)
add_python_style_test(pep8_style_gaia_rest
                      "${PROJECT_SOURCE_DIR}/plugins/gaia_minerva/server/rest")
