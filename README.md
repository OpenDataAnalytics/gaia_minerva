## Gaia - Minerva plugin

gaia_minerva is a Girder plugin that allows Gaia geospatial processes to be run on Minerva datasets via girder jobs.


#### Installation

In your girder plugins directory:
- pip install -e .
- pip install -r requirements.txt

Then log in to Girder as an admin and enable the plugin.



#### Demo use
The following is a sample Gaia process in JSON format, using the plugin's MinervaVectorIO class.
The item_id is the Girder item id of the Minerva dataset.
Raster datasets are not yet supported.


```
{
  "inputs": [
    {
      "_type": "girder.plugins.gaia_minerva.inputs.MinervaVectorIO",
      "item_id": "57b1f1c4f70ea27d9a25b8b2"
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



gaia_minerva [![Build Status](https://api.travis-ci.org/OpenDataAnalytics/gaia_minerva.svg?branch=master)](https://travis-ci.org/OpenDataAnalytics/gaia_minerva)  [![Documentation Status](https://readthedocs.org/projects/gaia/badge/?version=latest)](https://readthedocs.org/projects/gaia_minerva/?badge=latest) [![Join the chat at https://gitter.im/OpenGeoscience/gaia](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/OpenGeoscience/gaia?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)



#### License

Copyright 2015 Kitware Inc.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0


Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
