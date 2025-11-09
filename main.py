import argparse
import os
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Инструмент визуализации графа зависимостей (Этап 1)"
    )

    # Добавляем аргументы
    parser.add_argument("--package-name", type=str, required=True,
                        help="Имя анализируемого пакета")

    parser.add_argument("--repo-url", type=str, required=True,
                        help="URL-адрес репозитория или путь к файлу тестового репозитория")

    parser.add_argument("--mode", type=str, choices=["real", "test"], default="real",
                        help="Режим работы: real — с реальным репозиторием, test — с тестовым")

    parser.add_argument("--output-file", type=str, default="graph.png",
                        help="Имя файла для сохранения изображения графа")

    parser.add_argument("--ascii-output", action="store_true",
                        help="Вывод зависимостей в виде ASCII-дерева")

    parser.add_argument("--max-depth", type=int, default=3,
                        help="Максимальная глубина анализа зависимостей")

    args = parser.parse_args()

    # Проверка параметров и обработка ошибок
    errors = []

    if not args.package_name.strip():
        errors.append("Имя пакета не может быть пустым.")

    if args.mode == "real":
        if not args.repo_url.startswith("http"):
            errors.append("Для режима 'real' repo-url должен быть ссылкой (начинаться с http/https).")
    else:
        if not os.path.exists(args.repo_url):
            errors.append(f"Файл тестового репозитория не найден: {args.repo_url}")

    if args.max_depth <= 0:
        errors.append("Максимальная глубина анализа должна быть положительным числом.")

    # Если ошибки есть — вывести и завершить программу
    if errors:
        print("Ошибки конфигурации:")
        for err in errors:
            print(" -", err)
        sys.exit(1)

    return args


def main():
    args = parse_arguments()

    print("Параметры приложения:")
    print(f"Имя пакета = {args.package_name}")
    print(f"URL или файл репозитория = {args.repo_url}")
    print(f"Режим работы = {args.mode}")
    print(f"Файл вывода = {args.output_file}")
    print(f"Вывод ASCII = {args.ascii_output}")
    print(f"Максимальная глубина анализа = {args.max_depth}")
    print("\nРабота завершена успешно.")


if __name__ == "__main__":
    main()
