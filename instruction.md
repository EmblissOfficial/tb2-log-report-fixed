There is an Apache-style access log at `/app/access.log`.

Create a JSON report with these success criteria:

1. Save a valid JSON file at `/app/report.json`.
2. Include `total_requests` with the total number of non-empty log lines.
3. Include `unique_ips` with the number of distinct client IP addresses in the log.
4. Include `top_path` with the most frequently requested path in the log.
