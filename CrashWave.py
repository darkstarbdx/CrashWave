import requests
import concurrent.futures
import time
import random
import json
import os
import sys
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich.style import Style
from rich.box import ROUNDED

# Initialize Rich console
console = Console()

# Branding (Added)
TOOL_NAME = "CrashWave"
VERSION = "1.0"
AUTHOR = "Darkstarbdx"
GITHUB = "https://github.com/darkstarbdx"

# Function to clear the screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Large pool of user agents to bypass blocking
USER_AGENTS = [
    # Chrome on Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",

    # Chrome on macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",

    # Chrome on Linux
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",

    # Firefox on Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",

    # Firefox on macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:85.0) Gecko/20100101 Firefox/85.0",

    # Firefox on Linux
    "Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",

    # Safari on macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",

    # Edge on Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36 Edg/88.0.705.81",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",

    # Edge on macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36 Edg/88.0.705.81",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",

    # Android Chrome
    "Mozilla/5.0 (Linux; Android 11; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",

    # iOS Safari
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",

    # Android Firefox
    "Mozilla/5.0 (Android 11; Mobile; rv:89.0) Gecko/89.0 Firefox/89.0",
    "Mozilla/5.0 (Android 11; Mobile; rv:88.0) Gecko/88.0 Firefox/88.0",
    "Mozilla/5.0 (Android 11; Mobile; rv:87.0) Gecko/87.0 Firefox/87.0",
    "Mozilla/5.0 (Android 11; Mobile; rv:86.0) Gecko/86.0 Firefox/86.0",
    "Mozilla/5.0 (Android 11; Mobile; rv:85.0) Gecko/85.0 Firefox/85.0",

    # iOS Chrome
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/90.0.4430.78 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/89.0.4389.72 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/88.0.4324.104 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1",

    # Linux Firefox
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",

    # Windows Edge (Legacy)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",

    # Miscellaneous
    "Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko",  # IE11
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",  # IE11 on Windows 7
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",  # IE11 on Windows 8.1
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",  # Firefox on Windows 7
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",  # Firefox on Windows 8.1
]

# Function to get a random user agent
def get_random_user_agent():
    return random.choice(USER_AGENTS)

# Function to send a single HTTP request with retries and adaptive delays
def send_request(url, method="GET", headers=None, data=None, retries=3):
    for attempt in range(retries):
        try:
            # Add a random delay between retries
            if attempt > 0:
                time.sleep(random.uniform(0.5, 2.0))  # Random delay between 0.5 and 2 seconds

            # Set a random user agent
            headers = headers or {}
            headers["User-Agent"] = get_random_user_agent()

            if method == "GET":
                response = requests.get(url, headers=headers)
            elif method == "POST":
                if isinstance(data, dict):
                    headers["Content-Type"] = "application/json"
                    response = requests.post(url, headers=headers, json=data)
                else:
                    response = requests.post(url, headers=headers, data=data)
            else:
                return "Invalid method", 0

            # Check for WAF blocking (e.g., 403 or 429 status codes)
            if response.status_code in [403, 429]:
                console.print(f"[bold yellow]WAF blocked request. Retrying ({attempt + 1}/{retries})...")
                continue

            return response.status_code, response.elapsed.total_seconds()
        except requests.exceptions.RequestException as e:
            if attempt == retries - 1:
                return str(e), 0
            time.sleep(1)  # Wait before retrying
    return "Max retries reached", 0

# Function to perform load testing with adaptive behavior
def adaptive_load_test(url, num_requests, max_threads, method="GET", data=None, retries=3, min_delay=0.1, max_delay=1.0):
    start_time = time.time()
    results = []
    errors = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = []
        for i in range(num_requests):
            # Add a random delay between requests
            if i > 0:
                time.sleep(random.uniform(min_delay, max_delay))

            # Submit a request
            futures.append(executor.submit(
                send_request, url, method, None, data, retries
            ))

            # Monitor errors and adapt
            if len(errors) > 10:  # Stop if too many errors
                console.print("[bold red]Too many errors. Stopping test...")
                break

        # Wait for all futures to complete
        for future in concurrent.futures.as_completed(futures):
            status_code, response_time = future.result()
            if status_code == 200:
                results.append(response_time)
            else:
                errors.append(status_code)

    return results, errors, time.time() - start_time

# Function to display results in a Rich table
def display_results(url, results, errors, total_time, num_requests):
    successful_requests = len(results)
    failed_requests = len(errors)
    avg_response_time = sum(results) / successful_requests if successful_requests > 0 else 0

    # Results Panel
    results_table = Table(title="[bold]Test Results", box=ROUNDED, border_style="blue")
    results_table.add_column("Metric", style="cyan", justify="left")
    results_table.add_column("Value", style="white", justify="right")
    results_table.add_row("Target URL", url)
    results_table.add_row("Total Requests", str(num_requests))
    results_table.add_row("Successful Requests", str(successful_requests))
    results_table.add_row("Failed Requests", str(failed_requests))
    results_table.add_row("Average Response Time", f"{avg_response_time:.2f} seconds")
    results_table.add_row("Total Time", f"{total_time:.2f} seconds")
    results_table.add_row("Requests Per Second", f"{num_requests / total_time:.2f}")

    console.print(Panel(results_table, title="[bold green]Test Complete", border_style="green"))

    # Errors Panel
    if errors:
        error_table = Table(title="[bold]Errors", box=ROUNDED, border_style="red")
        error_table.add_column("Error", style="cyan", justify="left")
        error_table.add_column("Count", style="white", justify="right")
        error_counts = {error: errors.count(error) for error in set(errors)}
        for error, count in error_counts.items():
            error_table.add_row(str(error), str(count))
        console.print(Panel(error_table, title="[bold red]Error Summary", border_style="red"))

# Main function with a Rich UI
if __name__ == "__main__":
    try:
        clear_screen()

        # Header Panel with Branding (Added)
        header_panel = Panel(
            Text(f"{TOOL_NAME} v{VERSION}\n● Author: {AUTHOR}\n● Profile: {GITHUB}\n✘ Use it in your own risk", justify="left", style="bold white on red"),
            border_style="blue",
            box=ROUNDED,
            expand=False    
        )
        console.print(header_panel)

        # Input Panel
        url = console.input("[bold cyan]✦ Enter the target URL (e.g., https://example.com): ")
        num_requests = int(console.input("[bold cyan]✦ Enter the number of requests [default: 100]: ") or 100)
        max_threads = int(console.input("[bold cyan]✦ Enter the maximum number of concurrent threads [default: 10]: ") or 10)
        method = console.input("[bold cyan]✦ Enter the HTTP method (GET/POST) [default: GET]: ").upper().strip() or "GET"
        retries = int(console.input("[bold cyan]✦ Enter the number of retries for failed requests [default: 3]: ") or 3)
        mode = console.input("[bold cyan]✦ Enter the load test mode (constant/burst/ramp/random) [default: constant]: ").lower().strip() or "constant"

        data = None
        if method == "POST":
            data_input = console.input("[bold cyan]✦ Enter POST data (JSON format, e.g., {\"key\": \"value\"}): ")
            if data_input:
                try:
                    data = json.loads(data_input)
                except json.JSONDecodeError:
                    console.print("[bold red]Invalid JSON input. Using raw data.")
                    data = data_input

        clear_screen()

        # Progress Panel
        progress_panel = Panel(
            Text("Starting load test...", justify="center", style="bold green"),
            border_style="green",
            box=ROUNDED,
            expand=False
        )
        console.print(progress_panel)

        # Perform the load test based on the selected mode
        if mode == "constant":
            rate = float(console.input("[bold cyan]✦ Enter the request rate (requests per second) [default: 10]: ") or 10)
            results, errors, total_time = adaptive_load_test(url, num_requests, max_threads, method, data, retries, rate)
        elif mode == "burst":
            results, errors, total_time = adaptive_load_test(url, num_requests, max_threads, method, data, retries)
        elif mode == "ramp":
            ramp_time = float(console.input("[bold cyan]Enter the ramp-up time (seconds) [default: 10]: ") or 10)
            results, errors, total_time = adaptive_load_test(url, num_requests, max_threads, method, data, retries, ramp_time)
        elif mode == "random":
            min_delay = float(console.input("[bold cyan]Enter the minimum delay between requests (seconds) [default: 0.1]: ") or 0.1)
            max_delay = float(console.input("[bold cyan]Enter the maximum delay between requests (seconds) [default: 1.0]: ") or 1.0)
            results, errors, total_time = adaptive_load_test(url, num_requests, max_threads, method, data, retries, min_delay, max_delay)
        else:
            console.print("[bold red]Invalid mode. Using constant rate by default.")
            results, errors, total_time = adaptive_load_test(url, num_requests, max_threads, method, data, retries)

        # Display results
        display_results(url, results, errors, total_time, num_requests)

        # Footer Panel with Branding (Added)
        footer_panel = Panel(
            Text(f"{TOOL_NAME} v{VERSION} | By {AUTHOR} | {GITHUB}", justify="center", style="bold white on blue"),
            border_style="blue",
            box=ROUNDED,
            expand=False
        )
        console.print(footer_panel)

    except KeyboardInterrupt:
        console.print("\n[bold yellow]Load test interrupted by user. Exiting gracefully...")
        sys.exit(0)