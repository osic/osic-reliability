#!/usr/bin/env python
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This script calls the cinder API and gathers the volume group capacity
# information and outputs to Influx Protocol Line format

import argparse
from datetime import datetime
import json
import os
import socket
import subprocess

from influxdb import InfluxDBClient

INFLUXDB_HOST = os.environ.get("INFLUXDB_HOST", "localhost")
INFLUXDB_PORT = 8086
INFLUXDB_USER = 'root'
INFLUXDB_PWD = 'SuperSecrete'
INFLUXDB_DATABASE = 'telegraf'
RALLY_TASK_LIST = 'rally task list'
EGREP_UUID = ("egrep '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]"
              "{4}-[0-9a-f]{4}-[0-9a-f]{12}'")
AWK_CMD = "awk '{if($11 !=\"\") print $2}'"
TAIL_LAST = 'tail -n 1'


def parse_and_send_to_influx(rally_task_id):
    json_output = None
    influx_objects = []

    try:
        output = subprocess.check_output("source /opt/rally/bin/activate;"
                                         "/bin/bash -l -c "
                                         "'rally task results {}'"
                                         .format(rally_task_id),
                                         shell=True,
                                         stderr=subprocess.PIPE)
        json_output = json.loads(output)

    except subprocess.CalledProcessError as exception:
        output = exception.output

    if json_output:
        for task in json_output:

            for i, result in enumerate(task["result"]):
                influx_object = dict()
                influx_object['measurement'] = "rally_task"
                influx_object['tags'] = {
                    "host": socket.gethostname(),
                    'task_id': rally_task_id,
                    'scenario': task['key']['name']
                }
                influx_object['time'] = str(datetime.utcnow())
                influx_object['fields'] = {
                    'load_duration': task['load_duration'],
                    'full_duration': task['full_duration'],
                    'iteration': i,
                    'iteration_error': int(len(result['error']) > 0),
                    'iteration_timestamp': result['timestamp'],
                    'iteration_duration': result['duration'],
                    'iteration_idle_duration': result['idle_duration']
                }

                for j, key in enumerate(result['atomic_actions'].keys()):
                    name_key = 'iteration_atomic_action_name{}'.format(j)
                    duration_key = \
                        'iteration_atomic_action_duration{}'.format(j)
                    influx_object['fields'][name_key] = key
                    influx_object['fields'][duration_key] = \
                        result['atomic_actions'][key]

                influx_objects.append(influx_object)

        influx_c = InfluxDBClient(INFLUXDB_HOST,
                                  INFLUXDB_PORT,
                                  INFLUXDB_USER,
                                  INFLUXDB_PWD,
                                  INFLUXDB_DATABASE)
        influx_c.write_points(influx_objects)
        return 'Results written'

    return output


def main(args):
    task_id = args.rally_task_id

    if task_id is None:
        try:
            output = subprocess.check_output("source /opt/rally/bin/activate;"
                                             "{} | {} | {} | {}"
                                             .format(RALLY_TASK_LIST,
                                                     EGREP_UUID,
                                                     AWK_CMD,
                                                     TAIL_LAST),
                                             shell=True,
                                             stderr=subprocess.PIPE)
            print ("Using task: {}".format(output))
            task_id = output.strip()
            print ("Data successfully written to InfluxDB")
            parse_and_send_to_influx(task_id)
        except subprocess.CalledProcessError as exception:
            output = exception.output
            print ("ERROR: Failed to get last Rally task ID ")
            print (output)
            raise exception


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Rally Task To Influx")
    parser.add_argument('rally_task_id',
                        nargs='?',
                        default=None,
                        type=str,
                        help="Rally Task uuid")
    args = parser.parse_args()
    main(args)
