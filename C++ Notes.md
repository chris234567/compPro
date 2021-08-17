# C++ Notes

`#include <bits/stdc++.h>` ⇒ imports complete standard library

`using std` ⇒ shortens calls like  `std::cout`  to  `cout`

compile command: `g++ -std=c++11 -O2 -Wall test.cpp -o test`

- -std=c++11: compiler uses c++11 standard
- -02: code gets optimized
- -Wall: warnings will be shown

**Input:** `cin >> VARIABLE`>> .. 

- can be extended with at least one space between entries
- *Example:*

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

**Working with files:**

```cpp
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
```

### Numbers

**Most used numeric types:**

- $−2·10^9$  <  `int`  <  $2·10^9$  (32bit)   e.g.   `int i = 123;`
- $−9·10^{18}$  <  `long long`  <  $9·10^{18}$  (64bit)   e.g.   `long long l = 123LL;`

...