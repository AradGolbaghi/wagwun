import psutil
import os

# Optional: known suspicious keywords or module names
SUSPICIOUS_KEYWORDS = ["keylogger", "pynput", "keyboard", "hook", "logkeys"]

def detect_suspicious_processes():
    print("[*] Scanning running processes for suspicious activity...\n")
    found = False

    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmdline = ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else ""
            for keyword in SUSPICIOUS_KEYWORDS:
                if keyword.lower() in cmdline.lower():
                    print(f"[!] Suspicious process found: PID={proc.info['pid']} | Name={proc.info['name']}")
                    print(f"    Command Line: {cmdline}")
                    found = True
                    break
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if not found:
        print("[✓] No suspicious keylogging activity detected.")
    print()

if __name__ == "__main__":
    detect_suspicious_processes()
