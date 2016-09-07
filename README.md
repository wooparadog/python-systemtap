# Python binding for systemtap

## Build

Only for **Centos** or other redhat alternatives.

```
sudo yum install systemtap systemtap-devel systemtap-sdt-devel
make
```

## Usage

This library provide the following probe:

```
provider pystap {
  probe entry(char *, char *);
};
```

An easy decorator is implemented:

```python
from pystap import dtrace_deco

@dtrace_deco
def its_a_test(a_para, that_para=None):
    print a_para, that_para
```


## Example:

Usage is shown in `test.py`, execute bash command like following:

```bash
sudo stap  -e 'probe process.library("/home/vagrant/github/python-systemtap/libpystap.so").mark("entry"){printf("%s - %s", user_string($arg1), user_string($arg2))}'  -c "python test.py"
```

Note: You should manually give the location of `libpystap.so` to `stap`.

