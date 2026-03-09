# GCODEAdapterForKobraOS
Данный скрипт создан для возможности использования Gcode из OrcaSliser в 3d принтерах от AnyCubic на прошивке Klipper-Go, так как она использует древние команды Marlin для SET_VELOCITY_LIMIT, SET_PRESSURE_ADVANCE и SQUARE_CORNER_VELOCITY. Скрипт создан на основе TengerTechnologies/Smoothificator и использует python.
Для его установки необходимо необходимо написать текст в настройках профиля Прочее/Пост-Скрипт обработки в формате: "ПУТЬ ДО ФАЙЛА PYTHON.EXE" "ПУТЬ ДО СПРИПТА"
