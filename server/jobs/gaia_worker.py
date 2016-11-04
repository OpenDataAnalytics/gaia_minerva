#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#  Copyright Kitware Inc. and Epidemico Inc.
#
#  Licensed under the Apache License, Version 2.0 ( the "License" );
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
###############################################################################

import json
import re
import sys
import traceback
from gaia.parser import deserialize
from girder.utility.model_importer import ModelImporter
from girder.plugins.jobs.constants import JobStatus


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
                '_type':
                    'girder.plugins.gaia_minerva.inputs.MinervaVectorIO',
                'item_id': datasetId,
                'token': token['_id']
            }
        else:
            analysis['output']['item_id'] = datasetId
            analysis['output']['token'] = token['_id']

        process = json.loads(json.dumps(analysis), object_hook=deserialize)
        process.compute()
        job_model.updateJob(job, status=JobStatus.SUCCESS)
    except Exception:
        t, val, tb = sys.exc_info()
        log = '%s: %s\n%s' % (t.__name__, repr(val), traceback.extract_tb(tb))
        # TODO only works locally
        job_model.updateJob(job, status=JobStatus.ERROR, log=log)
        raise
