from rich.console import Console
from rich.table import Table
from datetime import datetime
import psutil
import socket

console = Console()

# System Information
hostname = socket.gethostname()
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

cpu_usage = psutil.cpu_percent(interval=1)
ram_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

network = psutil.net_io_counters()
connections = psutil.net_connections()

interfaces = psutil.net_if_addrs()

# Alerts
cpu_alert = "NORMAL"
ram_alert = "NORMAL"
disk_alert = "NORMAL"

if cpu_usage > 80:
    cpu_alert = "HIGH"

if ram_usage > 80:
    ram_alert = "HIGH"

if disk_usage > 80:
    disk_alert = "HIGH"

# Dashboard
table = Table(title="Linux Network Monitoring Tool")

table.add_column("Metric", style="cyan")
table.add_column("Value", style="green")

table.add_row("Timestamp", current_time)
table.add_row("Hostname", hostname)

table.add_row("CPU Usage", f"{cpu_usage}%")
table.add_row("CPU Alert", cpu_alert)

table.add_row("RAM Usage", f"{ram_usage}%")
table.add_row("RAM Alert", ram_alert)

table.add_row("Disk Usage", f"{disk_usage}%")
table.add_row("Disk Alert", disk_alert)

table.add_row("Bytes Sent", str(network.bytes_sent))
table.add_row("Bytes Received", str(network.bytes_recv))

table.add_row("Active Connections", str(len(connections)))
table.add_row("Network Interfaces", str(len(interfaces)))

console.print(table)

# Logging
with open("system.log", "a") as log:
    log.write(
        f"{current_time}, CPU={cpu_usage}%, RAM={ram_usage}%, "
        f"DISK={disk_usage}%, CONNECTIONS={len(connections)}\n"
    )
