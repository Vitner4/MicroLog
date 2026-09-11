<p align="center">

<img src="assets/logo.png" width="300" alt="MicroLog Logo">

</p>

<h1 align="center">MicroLog</h1>

<p align="center">
A lightweight logging library for Python focused on simplicity, efficiency, and predictable behavior.
</p>
---

[🇷🇺 Русская версия](README_RU.md)

---

## 📌 About

**MicroLog** is a small Python logging library designed around one idea: **do the job without unnecessary complexity**.

It provides basic log levels, console output, file output, enable/disable controls, and customizable log file paths while keeping the implementation compact and easy to understand.

## 🧩 Features

- **Three log levels:** `INFO`, `WARNING`, `ERROR`
- **Console output** with ANSI-colored log levels
- **File output** to a `.log` or text file
- **Timestamped log entries**
- **Visual level markers** using `🟢`, `🟡`, and `🔴`
- **Enable / disable logging** at runtime
- **Custom log file path** through `Path`
- **Automatic log file headers** for new logging sessions
- **Minimal dependency footprint** — built with the Python standard library

## 🔮 Philosophy

MicroLog is intentionally small.

The project does not try to replace feature-rich logging frameworks. Instead, it focuses on a limited set of useful features and keeps the architecture simple, readable, and predictable.

> **Small. Simple. Fast enough. Predictable.**

## 🕹️ Usage

Import `Logger` from the package:

```python
from microlog import Logger

log = Logger()

log.info("Good!")
log.warning("Look out!")
log.error("Error!!!")
```

### ▶️ Enable and disable logging

```python
log.disable()
log.info("This message will not be logged")

log.enable()
log.info("Logging is enabled again")
```

### 🛠️ Change the log file

```python
log.path = "./microlog.log"
log.info("Writing to a custom log file")
```

`path` accepts a filesystem path and is stored internally as a `pathlib.Path` object.

## 📤 Output

### 🖥️ Console

The console formatter colors the log level for quick visual recognition:

```text
[2026-09-11 23:29:27.529479] [INFO] - Good!
[2026-09-11 23:29:27.529547] [WARNING] - Look out!
[2026-09-11 23:29:27.529563] [ERROR] - Error!!!
```

`INFO`, `WARNING`, and `ERROR` are displayed with different ANSI colors.

### 📄 Log file

The file output keeps a readable text representation and adds a visual symbol for each level:

```text
___________________________[ 2026-09-12 ]___________________________
<< [2026-09-12 01:41:24.973005] [🟢] [INFO] - Good!
<< [2026-09-12 01:41:24.973137] [🟡] [WARNING] - Look out!
<< [2026-09-12 01:41:24.973173] [🔴] [ERROR] - Error!!!
```

A header is written when a new logging session starts for the current log path.

## 📊 Architecture

MicroLog intentionally uses a small architecture:

```text
Logger
  │
  └── Formatter
        ├── console()
        ├── file()
        └── headline()
```

### 📝 `Logger`

Responsible for the logging lifecycle and public API:

- `info()`
- `warning()`
- `error()`
- `enable()`
- `disable()`
- `path`

The private `_log()` method provides the common implementation used by all log levels.

### 🖌️ `Formatter`

Responsible for turning collected log data into formatted strings for console and file output.

The library deliberately avoids a larger hierarchy of handlers, factories, or other abstractions in order to keep the core small.

## 🗂️ Project structure

```text
MicroLog/
├── README.md
├── README_RU.md
├── LICENSE
├── .gitignore
└── microlog/
    ├── __init__.py
    ├── logger.py
    └── formatters.py
```

## ⚠️ Requirements

MicroLog is implemented with the Python standard library. No external logging dependency is required for the core library.

## ⚡ Status

**Version: 1.0.0**

MicroLog is intentionally a small project. Its feature set is limited by design.

## 📃 License

See [LICENSE](LICENSE.md) for the license terms.
