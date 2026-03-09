# Post-processing script for Klipper-Go based Anycubic printers who owners want to use Orca Slicer correctly
# Script version 1.5.0 based on /TengerTechnologies/Smoothificator and tested on Orca Slicer v2.3.1
# Changes SET_VELOCITY_LIMIT, SET_PRESSURE_ADVANCE and SQUARE_CORNER_VELOCITY for KobraOS compatible commands

# Скрипт постобработки для принтеров Anycubic на базе Klipper-Go, владельцы которых хотят правильно использовать Orca Slicer
# Скрипт версии 1.5.0 на основе /TengerTechnologies/Smoothificator, протестирован на Orca Slicer v2.3.1
# Изменены SET_VELOCITY_LIMIT, SET_PRESSURE_ADVANCE и SQUARE_CORNER_VELOCITY для команд, совместимых с KobraOS


import re
import argparse

def process_gcode(input_file):
    # Read the input G-code / Считывание G-code
    with open(input_file, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    # Process the G-code / Список, в который будет записываться изменённый код
    modified_lines = []

    for line in lines:
        # Detect Pressure Advance changes / Проверка кода на Pressure Advance
        if line.startswith("SET_PRESSURE_ADVANCE ADVANCE="):
            pa_line = re.sub(r"SET_PRESSURE_ADVANCE ADVANCE=", "M900 K", line)
            modified_pa_line = re.sub(r"; Override pressure advance value", " ;Override pressure advance value for KobraOS", pa_line)
            modified_lines.append(modified_pa_line)
        # Detect Velocity and SCV changes / Проверка кода на Velocity и SCV
        elif line.startswith("SET_VELOCITY_LIMIT"):
            modified_velocity_line = ""
            modified_SCV_line = ""
            if "ACCEL=" in line:
                velocity_match = re.search(r"([-\d.]+)", line)
                current_velocity = float(velocity_match.group(1))
                modified_velocity_line = re.sub(r".+", f"M204 S{current_velocity:.0f} ;Set velocity value for KobraOS", line)
            if "SQUARE_CORNER_VELOCITY=" in line:
                scv_match = re.search(r"(\d+)$", line)
                current_scv = float(scv_match.group(1))
                modified_SCV_line = re.sub(r".+", f"M205 X{current_scv:.0f} Y{current_scv:.0f} ;Set SCV value for KobraOS", line)
            modified_lines.append(modified_velocity_line + modified_SCV_line)
        else:
            modified_lines.append(line)

    # Overwrite the input file with the modified G-code / Запись строк в файл
    with open(input_file, "w") as outfile:
        outfile.writelines(modified_lines)

# Main execution / Основное выполнение
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process G-code file to modify velocity, PA and SCV for KobraOS")
    parser.add_argument("input_file", help="Input G-code file")
    args = parser.parse_args()
    process_gcode(input_file=args.input_file)