## Installation
Install the monitoring stack
`# ./install.sh`

## Send Task data to influx
1. `pip install influxdb`
2. `export INFLUXDB_HOST=<your influxdb host>`
3. activate rally virtual environment
4. `python send_task_data_to_influx.py` (will take the last task ID) OR `python send_task_data_to_influx.py <rally_task_id>`
5. you can run italong with a `rally task start` command: `rally task start <scenario>;python send_task_data_to_influx.py`