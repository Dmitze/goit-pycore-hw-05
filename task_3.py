import sys
from collections import Counter

def parse_log_line(line: str) -> dict:
    """Розбирає рядок логу на компоненти."""
    parts = line.strip().split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }

def load_logs(file_path: str) -> list:
    """Завантажує логи з файлу."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Використовуємо списковий вираз для компактності
            logs = [parse_log_line(line) for line in file]
        return logs
    except FileNotFoundError:
        print(f"Помилка: Файл '{file_path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []

def filter_logs_by_level(logs: list, level: str) -> list:
    """Фільтрує логи за вказаним рівнем."""
    return [log for log in logs if log['level'].lower() == level.lower()]

def count_logs_by_level(logs: list) -> dict:
    """Підраховує кількість записів для кожного рівня логування."""
    return Counter(log['level'] for log in logs)

def display_log_counts(counts: dict):
    """Виводить статистику логів у вигляді таблиці."""
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python task_3.py /шлях/до/logfile.log [рівень_логування]")
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if not logs:
        return

    display_log_counts(count_logs_by_level(logs))

    if len(sys.argv) > 2:
        level_to_filter = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level_to_filter)
        print(f"\nДеталі логів для рівня '{level_to_filter.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()