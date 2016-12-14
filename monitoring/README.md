## Installation
Install the monitoring stack
`# ./install.sh`

## Send Task data to influx
1. `pip install influxdb`
2. `export INFLUXDB_HOST=<your influxdb host>`
3. activate rally virtual environment
4. `python send_task_data_to_influx.py` (will take the last task ID) OR `python send_task_data_to_influx.py <rally_task_id>`
5. you can run italong with a `rally task start` command: `rally task start <scenario>;python send_task_data_to_influx.py`

## Rally Reports

The rally reports are being generated using a Jupyter notebook.

To run the reports do the following:
1. Backup the task data using the script `backup_rally_tasks.sh` which takes the rally deployment as an agurment
(i.e. `backup_rally_tasks.sh reliability`
2. Install Jupyter where you want to visualize the data: (http://jupyter.org/install.html)
`pip install jupyter`
3. cd into the directory where all the JSON task files are and run a new notebook server:
`jupyter notebook`
4. copy the `RallyReports.ipynb` in to the same folder where all the JSON task files are
5. browse hte notebook in your browser on port 8888
6. Execute