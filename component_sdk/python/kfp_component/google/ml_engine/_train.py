# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from fire import decorators
from ._create_job import create_job

@decorators.SetParseFns(python_version=str, runtime_version=str)
def train(project_id, python_module, package_uris, 
    region, args=None, job_dir=None, python_version=None, 
    runtime_version=None, training_input=None, job_id_prefix=None,
    wait_interval=30):
    """Creates a MLEngine training job.

    Args:
        project_id (str): Required. The ID of the parent project of the job.
        python_module (str): Required. The Python module name to run after 
            installing the packages.
        package_uris (list): Required. The Google Cloud Storage location of 
            the packages with the training program and any additional 
            dependencies. The maximum number of package URIs is 100.
        region (str): Required. The Google Compute Engine region to run the 
            training job in
        args (list): Command line arguments to pass to the program.
        job_dir (str): A Google Cloud Storage path in which to store training 
            outputs and other data needed for training. This path is passed 
            to your TensorFlow program as the '--job-dir' command-line 
            argument. The benefit of specifying this field is that Cloud ML 
            validates the path for use in training.
        python_version (str): Optional. The version of Python used in training. 
            If not set, the default version is '2.7'. Python '3.5' is 
            available when runtimeVersion is set to '1.4' and above. 
            Python '2.7' works with all supported runtime versions.
        runtime_version (str): Optional. The Cloud ML Engine runtime version 
            to use for training. If not set, Cloud ML Engine uses the 
            default stable version, 1.0. 
        training_input (dict): Input parameters to create a training job.
        job_id_prefix (str): the prefix of the generated job id.
        wait_interval (int): optional wait interval between calls
            to get job status. Defaults to 30.
    """
    if not training_input:
        training_input = {}
    if python_module:
        training_input['pythonModule'] = python_module
    if package_uris:
        training_input['packageUris'] = package_uris
    if region:
        training_input['region'] = region
    if args:
        training_input['args'] = args
    if job_dir:
        training_input['jobDir'] = job_dir
    if python_version:
        training_input['pythonVersion'] = python_version
    if runtime_version:
        training_input['runtimeVersion'] = runtime_version
    job = {
        'trainingInput': training_input
    }
    return create_job(project_id, job, job_id_prefix, wait_interval)