# GCODEAdapterForKobraOS

Скрипт для адаптации G-code из **Orca Slicer** под прошивку **Klipper-Go** на принтерах AnyCubic.

## Описание

Данный скрипт автоматически преобразует команды G-code, так как прошивка Klipper-Go использует устаревшие синтаксические конструкции Marlin для управления следующими параметрами:

* `SET_VELOCITY_LIMIT`
* `SET_PRESSURE_ADVANCE`
* `SQUARE_CORNER_VELOCITY`

Решение базируется на наработках [TengerTechnologies/Smoothificator](https://github.com/TengerTechnologies/Smoothificator) и требует установленного **Python**.

---

## Установка и настройка

Чтобы скрипт автоматически обрабатывал G-code после каждого слайсинга:

1. Откройте настройки вашего принтера в **Orca Slicer**.
2. Перейдите во вкладку **Настройки принтера** -> **Прочее**.
3. Найдите раздел **Пост-скрипт обработки**.
4. Добавьте путь к исполняемому файлу Python и путь к самому скрипту в следующем формате:

```Вот так вот, типо:
"ПУТЬ_К_PYTHON.EXE" "ПУТЬ_К_СКРИПТУ.py"

```

### Пример:

`"C:\Python310\python.exe" "C:\Scripts\anycubic_fix.py"`
