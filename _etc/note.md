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
