"""Простой скрипт для запуска тестов без pytest с гарантированным выводом"""
import sys
import os

# Добавляем текущую директорию в путь
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from test_evals import test_run_RAG

if __name__ == "__main__":
    print("=" * 60)
    print("Запуск теста run_RAG")
    print("=" * 60)
    try:
        test_run_RAG()
        print("\n✅ Тест выполнен успешно!")
    except Exception as e:
        print(f"\n❌ Ошибка при выполнении теста: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

