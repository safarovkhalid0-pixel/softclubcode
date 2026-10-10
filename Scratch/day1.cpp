#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    setlocale(LC_ALL, "Russian");

    srand(time(0));              // инициализация генератора случайных чисел
    int secret = rand() % 100 + 1; // число от 1 до 100
    int guess;

    cout << "Я загадал число от 1 до 100.\n";
    cout << "Попробуй угадать!\n";

    do {
        cout << "Введи число: ";
        cin >> guess;

        if (guess > secret) {
            cout << "Слишком большое!\n";
        } else if (guess < secret) {
            cout << "Слишком маленькое!\n";
        } else {
            cout << "🎉 Ты угадал! Молодец!\n";
        }
    } while (guess != secret);

    return 0;
}

