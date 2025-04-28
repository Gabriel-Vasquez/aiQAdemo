import os
import json
from utils.helpers import init_driver, collect_page_data
from sanitizer.sanitizer import sanitize_data
from datetime import datetime

def main():
    target_url = "http://automationpractice.com"
    run_folder = f"runs/{datetime.now().strftime('%Y%m%d_%H%M')}_demo"
    os.makedirs(run_folder, exist_ok=True)

    driver = init_driver()
    try:
        raw_data = collect_page_data(driver, target_url)
        with open(f"{run_folder}/raw_data.json", "w") as f:
            json.dump(raw_data, f, indent=4)
        sanitized = sanitize_data(raw_data)
        with open(f"{run_folder}/sanitized_data.json", "w") as f:
            json.dump(sanitized, f, indent=4)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()