import sys
from collections import Counter

def parse_log_line(line):
    parts = line.split(' ', 3)
    if len(parts) < 4:
        return None
    return {"date": parts[0], "time": parts[1], "level": parts[2], "message": parts[3].strip()}

def load_logs(file_path):
    with open(file_path, 'r') as file:
        return [parse_log_line(line) for line in file if parse_log_line(line)]

def filter_logs_by_level(logs, level):
    return [log for log in logs if log["level"].upper() == level.upper()]

def count_logs_by_level(logs):
    return Counter(log["level"] for log in logs)

def display_log_counts(counts):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<15} | {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Вкажіть шлях до файлу логів.")
        sys.exit(1)

    log_file = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        logs = load_logs(log_file)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

        if log_level:
            filtered_logs = filter_logs_by_level(logs, log_level)
            print(f"\nДеталі логів для рівня '{log_level.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
    except FileNotFoundError:
        print("Файл логів не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
