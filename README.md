# GCODEAdapterForKobraOS 🐍

With the author's permission ([Satmosftk2](https://github.com/Satmosftk2)), I am using his work here for further modification

Script for adapting G-code from **Orca Slicer** to **Klipper-Go** firmware on AnyCubic printers.

## Description 🤔
This script automatically converts G-code commands, as the Klipper-Go firmware uses outdated Marlin syntaxes to control the following parameters:

* `SET_VELOCITY_LIMIT`
* `SET_PRESSURE_ADVANCE`
* `SQUARE_CORNER_VELOCITY`

The solution is based on the work of [TengerTechnologies/Smoothificator](https://github.com/TengerTechnologies/Smoothificator) and requires an installed **Python** 🐍✨.

---

## Installation and Configuration (Instructions for Humans)

To make the script automatically process the G-code after each slicing:

1. Open your printer settings in **Orca Slicer**.
2. Go to the **Process** tab -> **Other**.
3. Find the **Post-processing Scripts** section.
4. Add the path to the Python executable file and the path to the script itself in the following format:

```Bash
"PATH_TO_PYTHON.EXE" "PATH_TO_SCRIPT.py"

```

### Пример:

`"C:\Python310\python.exe" "C:\Scripts\KobraOSadapter.py"`
