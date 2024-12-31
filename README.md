# **UNDER CONSTRUCTION!**

# **CrashWave** 🌊

**CrashWave** is a powerful Python-based load testing tool designed to simulate high traffic on websites or web applications. With its **Rich UI**, **adaptive load testing modes**, and **detailed reporting**, **CrashWave** helps developers and DevOps engineers test the performance, scalability, and resilience of their systems under heavy load. Whether you’re testing a single endpoint or a complex web application, **CrashWave** provides the tools you need to ensure your system can handle real-world traffic.

---

## **Features** ✨
- **Rich UI**: Beautiful and interactive terminal interface powered by the `rich` library.
- **Load Test Modes**:
  - **Constant**: Sends requests at a constant rate.
  - **Burst**: Sends requests in bursts to simulate sudden traffic spikes.
  - **Ramp**: Gradually increases the request rate over time.
  - **Random**: Sends requests with random delays for realistic traffic simulation.
- **Multi-Threaded**: Sends concurrent requests using a dynamic thread pool.
- **Randomized User Agents**: Simulates real users with a large pool of user agent strings.
- **Retry Mechanism**: Automatically retries failed requests.
- **Adaptive Behavior**: Adjusts request delays and retries based on server responses.
- **Detailed Reporting**: Provides success rates, average response times, and error summaries.
- **Real-Time Progress**: Displays progress using a `tqdm` progress bar.

---

## **Warning** ⚠️
**CrashWave is intended for ethical and authorized use only.**  
- **Permission**: Always obtain explicit permission before testing any website or application.  
- **Legal Compliance**: Unauthorized use of this tool may violate laws and regulations.  
- **Responsibility**: The user assumes full responsibility for any consequences of using this tool.  

---

## **Disclaimer** 🤖
This tool was developed with the assistance of **AI (Artificial Intelligence)**. While it has been thoroughly tested, please use it at your own risk and ensure it aligns with your ethical and legal standards.

---

## **Installation** 🛠️
1. Clone the repository:
   ```bash
   git clone https://github.com/darkstarbdx/CrashWave.git
   cd CrashWave
   ```
2. Install the required dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

---

## **Requirements** 📦
The required Python packages are listed in `requirements.txt`:
```plaintext
requests==2.31.0
rich==13.4.2
```

Install them using:
```bash
pip3 install -r requirements.txt
```

---

## **Usage** 🚦
Run the script and provide the required inputs:
```bash
python3 CrashWave.py
```

### **Inputs**:
- **Target URL**: The URL to test (e.g., `https://example.com`).
- **Number of Requests**: Total number of requests to send.
- **Max Threads**: Maximum number of concurrent threads.
- **HTTP Method**: `GET` or `POST`.
- **Retries**: Number of retries for failed requests.
- **Load Test Mode**: Choose from `constant`, `burst`, `ramp`, or `random`.
- **Request Rate/Delays**: Configure based on the selected mode.

### **Example**:
```plaintext
✦ Enter the target URL (e.g., https://example.com): https://example.com
✦ Enter the number of requests [default: 100]: 100
✦ Enter the maximum number of concurrent threads [default: 10]: 10
✦ Enter the HTTP method (GET/POST) [default: GET]: GET
✦ Enter the number of retries for failed requests [default: 3]: 3
✦ Enter the load test mode (constant/burst/ramp/random) [default: constant]: constant
✦ Enter the request rate (requests per second) [default: 10]: 10
```

---

## **Load Test Modes** 🔥
- **Constant**: Sends requests at a fixed rate (e.g., 10 requests per second).
- **Burst**: Sends a large number of requests in a short period to simulate traffic spikes.
- **Ramp**: Gradually increases the request rate over time to test system scalability.
- **Random**: Sends requests with random delays for more realistic traffic simulation.

---

## **Output** 📊
The tool provides a detailed summary of the load test, including:
- Total requests
- Successful requests
- Failed requests
- Average response time
- Total time
- Requests per second
- Error summary (if any)

---

## **Example Output** 📄
```plaintext
Test Results:
● Target URL: https://example.com
● Total Requests: 100
● Successful Requests: 98
● Failed Requests: 2
● Average Response Time: 0.25 seconds
● Total Time: 6.12 seconds
● Requests Per Second: 16.34

Error Summary:
● 404: 2 occurrences
```

---

## **Contributing** 🤝
Contributions are welcome! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

---

## **License** 📜
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## **Credits** 🙏
This tool was developed with the assistance of **AI (Artificial Intelligence)**.

---

## **Support** 💬
If you have any questions or need help, feel free to open an issue or contact the maintainers.
✨ Want to get in touch?
🌟 Join our vibrant Telegram community!
👉 Click here to connect: [Telegram Group](https://t.me/+mzZ9IrWgXe9jNWNl)

---

**Happy Testing with CrashWave!** 🌊🚀
