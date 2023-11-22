import os

# Отримати значення змінної середовища SSLKEYLOGFILE
ssl_keylog_file = os.getenv("SSLKEYLOGFILE")

# Перевірити, чи змінна була створена
if ssl_keylog_file is not None:
    print("Змінна середовища SSLKEYLOGFILE створена.")
    print(f"Значення: {ssl_keylog_file}")
else:
    print("Змінна середовища SSLKEYLOGFILE не була створена.")
