# Copyright (c) 2015 P. Michiardi, D. Venzano
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from sahara.service.edp import base_engine
from sahara.utils import edp


class NullJobEngine(base_engine.JobEngine):
    def cancel_job(self, job_execution):
        pass

    def get_job_status(self, job_execution):
        pass

    def run_job(self, job_execution):
        return 'oozie_job_id', edp.JOB_STATUS_SUCCEEDED, None

    def validate_job_execution(self, cluster, job, data):
        pass

    @staticmethod
    def get_possible_job_config(job_type):
        return None

    @staticmethod
    def get_supported_job_types():
        return edp.JOB_TYPES_ALL
