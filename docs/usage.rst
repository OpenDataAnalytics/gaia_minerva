Gaia-Minerva Usage
=====================================================

From the Minerva webpage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Click on 'Gaia process' in the Minerva 'Analyses' tab to bring up the Gaia Process widget.
- Enter a name for your output dataset and select from the available processes.
- Once you select a process, choose the GeoJSON or WMS dataset(s) you would like to use as inputs
- Fill in values for whatever arguments the process may require.
- Click the Submit button.

The process will be added to the jobs queue, and once finished the result should appear in the
Datasets tab.

From the Girder web API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To manually create and run Gaia processes from the Girder API, use the '/gaia_analyses' endpoint.

This call requires a JSON body containing the output dataset name as well as a nested JSON structure
describing the process to run and its inputs and arguments.

For example:

::

    {
        "datasetName": "Demo Gaia Process Output"
        "process": {
          "inputs": [
            {
              "_type": "girder.plugins.gaia_minerva.inputs.MinervaVectorIO",
              "item_id": "57b1fe4ef70ea28b9ffae78a"
            },
            {
              "_type": "girder.plugins.gaia_minerva.inputs.MinervaVectorIO",
              "item_id": "57b1f1d2f70ea27d9a25b8b5"
            }
          ],
          "_type": "gaia.geo.IntersectsProcess"
        }
    }

