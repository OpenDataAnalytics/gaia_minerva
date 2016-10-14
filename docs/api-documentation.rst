API Documentation
=================

The gaia-minerva plugin provides a few Girder API endpoints:

- /gaia/analysis
    - Runs a Gaia process on data stored within Minerva, using the plugin's 'MinervaVectorIO' input class.  For example:

      ::

        {
          "_type": "gaia.geo.IntersectsProcess"
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
        }

    - The 'item_id' refers to the item id of the Minerva dataset

- /gaia_process/classes (GET)
    - Gets a list of available Gaia processes that can be run in Minerva, along with their required inputs and arguments

- /gaia_process (POST)
    - accepts a JSON body as input which describes the Gaia process to run, along with required inputs and arguments.  For example:

      ::

        {
          "_type": "gaia.geo.WithinProcess",
          "inputs": [
              {
                  "_type": "gaia.inputs.FeatureIO",
                  "features": {
                    "type": "FeatureCollection",
                    "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },

                    "features": [
                        { "type": "Feature", "properties": { "id": null, "city": "Denver" }, "geometry": { "type": "Point", "coordinates": [ -104.980333187279328, 39.7915589633457 ] } },
                        { "type": "Feature", "properties": { "id": null, "city": "Boulder" }, "geometry": { "type": "Point", "coordinates": [ -105.263511569948491, 40.019696278861431 ] } },
                        { "type": "Feature", "properties": { "id": null, "city": "Estes Park" }, "geometry": { "type": "Point", "coordinates": [ -105.530115377293299, 40.375433303596949 ] } }
                    ]
                    }
              },
              {
                  "_type": "gaia.inputs.ProcessIO",
                  "process": {
                      "_type": "gaia.geo.BufferProcess",
                      "inputs": [
                          {
                              "_type": "gaia.inputs.FeatureIO",
                              "features": [
                                  { "type": "Feature", "properties": { "id": null, "pathname": "denver to boulder" }, "geometry": { "type": "LineString", "coordinates": [ [ -105.255283057376104, 40.032298290353467 ], [ -104.968930819857619, 39.802577480692939 ] ] } }
                                ]
                          }
                      ],
                      "buffer_size": 10000
                  }
              }
          ],
            "output": {
                "_type": "gaia.inputs.FeatureIO"
            }
        }



