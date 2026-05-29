from rich.console import Console
from rich.table import Table
import psutil

console = Console()

table = Table(title="Linux Network Monitoring Tool")

table.add_column("Metric")
table.add_column("Value")

table.add_row("CPU Usage", f"{psutil.cpu_percent(interval=1)}%")
table.add_row("RAM Usage", f"{psutil.virtual_memory().percent}%")
table.add_row("Disk Usage", f"{psutil.disk_usage('/').percent}%")

network = psutil.net_io_counters()

table.add_row("Bytes Sent", str(network.bytes_sent))
table.add_row("Bytes Received", str(network.bytes_recv))

connections = psutil.net_connections()

table.add_row("Connections", str(len(connections)))

console.print(table)
