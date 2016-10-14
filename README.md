## Gaia - Minerva plugin

gaia_minerva is a Girder plugin that allows Gaia geospatial processes to be run on Minerva datasets via girder jobs.

Official documentation is available at http://gaia-minerva-plugin.readthedocs.io/

#### Installation

Make sure that you install and activate the Minerva plugin first.

Afterward, in your girder plugins directory:

```
git clone https://github.com/OpenDataAnalytics/gaia_minerva.git
cd gaia_minerva
pip install -e .
pip install -r requirements.txt
```

Then log in to Girder as an admin and enable the plugin.

Finally, you will need to run the Minerva 'import_analyses.py' to enable Gaia analyses in Minerva.
From the girder plugins directory:

```
cd minerva/utility
python import_analyses.py --username <username> --password <password> --host <girder_host> --port <girder_port> --path ../../gaia_minerva/analyses/gaia/
```

Use a Girder admin username and password to run the above command.

### Minerva UI usage
In Minerva's analyses tab, 'Gaia process' should now be visible.  Click on it to bring up the Gaia Process widget.
Enter a name for your output dataset and select from the available processes.
Once you select a process, choose the GeoJSON or WMS dataset(s) you would like to use as inputs,
and fill in values for whatever arguments the process may require.  Then click the Submit button.
The process will be added to the jobs queue, and once finished the result should appear in the
Datasets tab.



#### API use
The following is a sample Gaia process in JSON format, using the plugin's MinervaVectorIO class.
The item_id is the Girder item id of the Minerva dataset.
Raster datasets are not yet supported.


```
{
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
```

To run this process, post a request to http://<girder_url>/api/v1/gaia_analysis/, with the following parameters:

- datasetName = name of the output item/file
- token = authentication token string
- process = the above JSON

Example:

```
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
```

gaia_minerva [![Build Status](https://api.travis-ci.org/OpenDataAnalytics/gaia_minerva.svg?branch=master)](https://travis-ci.org/OpenDataAnalytics/gaia_minerva)  [![Documentation Status](https://readthedocs.org/projects/gaia/badge/?version=latest)](https://readthedocs.org/projects/gaia_minerva/?badge=latest) [![Join the chat at https://gitter.im/OpenGeoscience/gaia](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/OpenGeoscience/gaia?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)



#### License

Copyright 2015 Kitware Inc. and Epidemico Inc.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0


Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
