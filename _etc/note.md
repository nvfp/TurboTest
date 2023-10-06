- ~~fails and errors are combined together as "FAIL"~~ (not anymore @ oct4, 2023)
- To make things more confidently maintainable, TurboTest uses `unittest` (not TurboTest itself) as the testing framework.



ideal TurboTest dir tree:
```txt
my_project/        <~~ project root
└── my_project/    <~~ project distribution
    └── module_1/
        └── __init__.py
        └── test.py
    └── module_2/
        └── foo/
            └── __init__.py
            └── test.py
        └── bar/
            └── __init__.py
            └── test.py
        └── __init__.py
        └── test.py
    └── __init__.py
    └── __main__.py
└── LICENSE
└── README.md
```


~~when reporting string, 10,000 char is max, the middle chars will be replaced with "X more chars"~~  ->  when reporting string, ~~5,000~~ 10,000 char is max, the middle chars will be replaced with "X more chars"

- ~~All reported strings must be represented using the `repr` function.~~  ->  ~~all reported strings should be printed as the original, not as `repr`, for easier debugging~~ -> all reported string should be printed using `repr` to prevent the string from being improperly truncated (if they have escaped chars).
