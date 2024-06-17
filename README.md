## PyTest_documentation
1. Need to create a new directory in under dir all files are present.
2. Pytest file name start with test_ (test_demo.py)
3. Test method start with test(def test_program1())
4. -v verbose provide more information
5. -s use for print
6. -k  ->use for method name execution(pytest -k creditcard -v -s)
7. -m  mark use for tag test & sanity test (pytest -m samity -v -s)  
8. @pytest.mark.skip -> skip the test method
9. @pytest.mark.xfail -> not pass and not fail
10. @pytest.fixture() -> use in selenium for open/close browser
11. Report -> pytest --html=report.html  (pip install pytest-html)
12. -rA -> complete summary

**Program1 >>** test_demo.py
```
import pytest
def test_first_program():
   msg="Hi"
   assert msg == "Hi"
```
**Run->** pytest  test_demo.py -v -s 

**Program2 >>**  Skip 
```
import pytest
@pytest.mark.skip
def test_add():
   a=4
   assert a+2 ==6


def test_first_program():
   msg="Hi"
   assert msg == "Hi" 
```

**Program3** pytest -k -sanity -v -s
```
import pytest

@pytest.mark.skip
def test_add():
   a=4
   assert a+2 ==6


def test_first_program():
   msg="Hi"
   assert msg == "Hi" 


@pytest.mark.sanity
def test_conf():
   print("Hello")
```

**Run ->** pytest -k sanity -v -s

**Program4 >>** Xfail
```
import pytest
# @pytest.mark.skip
# def test_add():
#     a=4
#     assert a+2 ==6


# def test_first_program():
#     msg="Hi"
#     assert msg == "Hi" 


# @pytest.mark.sanity
# def test_conf():
#    print("Hello")   


@pytest.mark.conf
def test_second_program():
   msg="Bye"
   assert msg == "hi"   
@pytest.mark.xfail
def test_third_program():
   msg="Hello"
   assert msg == "Hello" 
````

**Run >>** pytest -v -s 


**Program5 >>** Fixture

```
import pytest


@pytest.fixture()
def set():
   print("Execute First")
   yield
   print("Execute Last")

def test_fixture_demo(set):
   print("Execute Second")
```
