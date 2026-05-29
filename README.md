# Linux Network Monitoring Tool

A Linux-based system monitoring tool developed using Python, psutil, Bash scripting, and cron automation.

## Features

- CPU usage monitoring
- RAM usage monitoring
- Disk usage monitoring
- Network traffic monitoring
- Active connection monitoring
- Terminal dashboard using Rich
- Automated execution using Bash scripts
- Scheduled monitoring using cron jobs
- Log generation for system statistics

## Technologies Used

- Python 3
- psutil
- Rich
- Bash
- Linux (Ubuntu 24.04 WSL)
- Cron
- Git & GitHub

## Installation

Clone the repository:

```bash
git clone https://github.com/gs27304/Linux-Network-Monitoring-Tool.git
```

Install dependencies:

```bash
pip install psutil rich
```

Run:

```bash
python3 monitor.py
```

## Sample Output

Displays:

- CPU Usage
- RAM Usage
- Disk Usage
- Bytes Sent
- Bytes Received
- Active Connections

## Future Improvements

- Real-time refresh dashboard
- Email alerts
- Flask web dashboard
- SNMP monitoring
- Network interface statistics
- Export reports to CSV


