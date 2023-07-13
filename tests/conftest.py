from test_foocompare import Foo

# 为失败的断言定义你自己的解释 pytest tests\\test_foocompare.py
def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return [
            "Comparing Foo instances:",
            "   vals: {} != {}".format(left.val, right.val),
        ]