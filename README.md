# Pico UEFI Developer Kit

![](logo.png)

This is a developer kit for UEFI applications to simplify UEFI development, the reason why we made Pico is because alot of UEFI developer kits are complex, hard to use, and so we decided to take it on us to make it easier for developers to get started with UEFI development.

## What Python interpreter is ported?

CPython is used in the Pico UEFI Developer Kit, CPython is a popular and widely used Python interpreter. CPython is good because it is mature, and allows you to develop Python applications on the Pico UEFI platform, and it is open source, allowing you to modify its source code.

## Process Manager

The process manager is useful for getting PC information, and listing directories in the Pico UEFI platform.

### Grabbing CPU counts

```python
import processmgr.mgr as mgr

mgr.Process.cpu_count(disableprint=False)
```

### Listing directories

```python
import processmgr.mgr as mgr

mgr.Process.list(disableprint=False)
```

## The same thing (but disableprint is true)

```python
import processmgr.mgr as mgr

mgr.Process.list(disableprint=True)
```

```python
import processmgr.mgr as mgr

mgr.Process.cpu_count(disableprint=True)
```
