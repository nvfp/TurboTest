# *TurboTest🔥*

let's make test readable and simple


## Give it a try

```python
import TurboTest as tt
from my_module.my_function import my_function

def basic_operations():
    result = my_function(2, 3)
    expected = 5
    tt.both_are_equal(result, expected)

def should_raise_AssertionError_for_input_less_than_25():
    with tt.these_will_raise(AssertionError) as its: my_function(21)
    tt.both_are_equal(its.exception_msg, "Invalid: Value is less than 25.")
```

What you will get:

```txt
TurboTest... at '/path/to/my_module'  (Monday, Jan 1, 2024, 13:11:21 UTC-0800)
────────────────────────────────────────────────────────────────────────────────────────────
[22:00:00] PASS: my_function: basic operation  (3|1m2.3s)
[22:00:02] PASS: my_function: should raise AssertionError for input less than 25  (9|2m2.1s)
[22:02:00] FAIL: abc123/foo/bar: should do X  (2|0m5.1s)
[22:03:00] FAIL: abc123/foo/bar: reject empty string  (1|0m0.1s)
[22:05:12] PASS: xyz/abc: exit if X equal to None  (9|0m0.7s)
[22:07:45] FAIL: xyz/pqr: return None if Y does not exist  (6|2m3.1s)
────────────────────────────────────────────────────────────────────────────────────────────
Done, 100 test functions [pass/fail: 61/39] executed in [core/total: 31m2.0s/37m3.1s] 🔥🔥
```

with color:

[]


## Install

- via PyPI: run `pip install turbotest`

## Misc

- [Thank you💙](https://nvfp.github.io/thank-you)
- [Documentation](https://nvfp.github.io/mykit)
- [Changelog](https://nvfp.github.io/mykit/changelog)


## License

This project's source code and documentation are under the MIT license.
