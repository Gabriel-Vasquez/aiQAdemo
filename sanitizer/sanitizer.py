def sanitize_data(raw_data):
    sanitized = {
        "pages_crawled": len(raw_data.get("pages", [])),
        "average_load_time_ms": sum(p['load_time'] for p in raw_data.get("pages", [])) / len(raw_data.get("pages", [])),
        "total_console_errors": sum(len(p['console_errors']) for p in raw_data.get("pages", [])),
        "ui_summary": [
            {
                "page": p['page_title'],
                "buttons": len(p['elements'].get('buttons', [])),
                "links": len(p['elements'].get('links', []))
            } for p in raw_data.get("pages", [])
        ]
    }
    return sanitized