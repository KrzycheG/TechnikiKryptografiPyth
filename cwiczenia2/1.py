import hashlib
import time

data = input("Podaj dane wejściowe: ")

# Iteruj przez wszystkie dostępne funkcje skrótu w bibliotece hashlib
for algorithm in hashlib.algorithms_available:
    # Stwórz obiekt haszujący dla danej funkcji skrótu
    hasher = hashlib.new(algorithm)

    # Rozpocznij pomiar czasu
    start_time = time.time()

    # Zaktualizuj wartość hasza na podstawie danych wejściowych
    hasher.update(data.encode())

    # Zakończ pomiar czasu
    end_time = time.time()

    # Wyświetl nazwę funkcji skrótu, wartość hasza i czas hashowania
    print(f"{algorithm}: {hasher.hexdigest()} ({end_time - start_time:.6f} s)")