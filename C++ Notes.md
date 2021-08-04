# C++ Notes

`#include <bits/stdc++.h>` ⇒ importiert komplette standard bibliothek

`using std` ⇒ verkürzt Aufrufe wie `std::cout` zu `cout`

compile command: `g++ -std=c++11 -O2 -Wall test.cpp -o test`

- -std=c++11: compiler verwendet c++11 standard
- -02: code wird optimiert
- -Wall: warnings werden gezeigt

**Input:** `cin >> VARIABLE`>> .. 

- kann erweitert werden pro mit mind. 1 Leerzeichen getrenntem Eintrag
- *Beispiel:*

    Input file

    ```
    123 456 monkey

    **oder**

    123   456
    monkey
    ```

    Code

    ```cpp
    *--- read words split by spaces ---*

    int a, b;
    string s;

    cin >> a >> b >> s;

    *--- read lines (split by "\n") ---*

    string s;
    getline(cin, s);
    ```

**Output:** `cout << VARIABLE`<< .. 

- *Beispiel:*

    ```cpp
    int a = 1, b = 2;
    string s = "world";

    cin << a << " " << b << " " << s;
    ------
    *1 2 world*
    ```

- snippet to optimize I/O

    ```cpp
    ios::sync_with_stdio(0);
    cin.tie(0);
    ```

*printf/scanf faster but more difficult to use
