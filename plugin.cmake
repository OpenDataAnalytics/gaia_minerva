add_python_test(geoprocess PLUGIN gaia_minerva)
add_python_test(geoservice_proxy PLUGIN gaia_minerva)
add_python_style_test(pep8_style_gaia_rest
                      "${PROJECT_SOURCE_DIR}/plugins/gaia_minerva/server/rest")
