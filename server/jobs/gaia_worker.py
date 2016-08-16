import json
import re
import sys
import traceback
from gaia.parser import deserialize
from girder.utility.model_importer import ModelImporter
from girder.plugins.jobs.constants import JobStatus
from gaia.core import GaiaException


def get_minerva_meta(client, id):
    """
    Get metadata about a Minerva Item from Girder
    """
    dataset_url = '/minerva_dataset/{}/dataset'.format(id)
    return client.get(dataset_url)


def save_geojson(client, meta, outpath):
    """
    Save GeoJSON from a Minerva item
    TODO: Use caching like the girder_worker.girder_io plugin
    TODO: Separate methods for saving geojson from different sources
    TODO: Develop method for downloading geojson via WFS calls for WMS vector layers
    """
    if 'geojson_file' in meta:
        # Uploaded GeoJSON is stored as a file in Girder
        client.downloadFile(meta['geojson_file']['_id'], outpath)
        with open(outpath, 'r') as jsonfile:
            geojson = json.load(jsonfile)
    elif 'geojson' in meta:
        # Mongo collection is stored in item meta
        geojson = json.loads(meta['geojson']['data'])
        with open(outpath, 'w') as outjson:
            json.dump(geojson, outjson)
    elif 'dataset_type' in meta and meta['dataset_type'] == 'wms':
        # Need to download geojson via WFS GetFeatures
        pass
    else:
        raise GaiaException('Unsupported Item Type')


def run(job):
    job_model = ModelImporter.model('job', 'jobs')
    job_model.updateJob(job, status=JobStatus.RUNNING)

    try:
        kwargs = job['kwargs']
        datasetId = str(kwargs['dataset']['_id'])
        token = kwargs['token']
        analysis = json.loads(kwargs['analysis'])

        for input in analysis['inputs']:
            input['token'] = token['_id']

        filename = re.sub('\s|\.', '_', kwargs['dataset']['name'])
        filename = '{}.json'.format(
            ''.join([c for c in filename if re.match(r'\w', c)]))

        if 'output' not in analysis:
            analysis['output'] = {
                'filename': filename,
                '_type': 'girder.plugins.gaia_minerva_plugin.inputs.MinervaVectorIO',
                'item_id': datasetId,
                'token': token['_id']
            }
        else:
            analysis['output']['item_id'] = datasetId
            analysis['output']['token'] = token['_id']

        process = json.loads(json.dumps(analysis), object_hook=deserialize)
        process.compute()
        job_model.updateJob(job, status=JobStatus.SUCCESS)
    except Exception as e:
        t, val, tb = sys.exc_info()
        log = '%s: %s\n%s' % (t.__name__, repr(val), traceback.extract_tb(tb))
        # TODO only works locally
        job_model.updateJob(job, status=JobStatus.ERROR, log=log)
        raise
