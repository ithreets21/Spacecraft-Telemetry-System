# Spacecraft Information

spacecraft_name = "Orion"
mission_name = "Artemis"

# Sensor Readings

sensor_readings = {
    "Temperature": 72,
    "Oxygen": 21,
    "Battery": 85,
    "Fuel": 64
}
print(spacecraft_name, mission_name)
def display_sensors():
    for sensor, reading in sensor_readings.items():
        print(sensor, reading)
display_sensors()

def calculate_average(): 
    total_readings = sum(sensor_readings.values())
    average_reading = total_readings / len(sensor_readings)
    print(average_reading)

calculate_average()

def check_sensor_status():
    for sensor, reading in sensor_readings.items():
        if reading < 50:
            print(sensor, "Warning")
        else:
            print(sensor, "Normal")

check_sensor_status()

sensor_limits = {
    "Temperature": 60,
    "Oxygen": 19,
    "Battery": 30,
    "Fuel": 25
}
def check_sensor_limits():
    for sensor, reading in sensor_readings.items():
        print("\n--- SENSOR STATUS REPORT ---")

    warning_count = 0

    for sensor, reading in sensor_readings.items():

        limit = sensor_limits[sensor]

        if reading < limit:

            print(sensor, ": WARNING")

            warning_count = warning_count + 1

        else:

            print(sensor, ": NORMAL")

    return warning_count


# 7. DISPLAY OVERALL MISSION STATUS

def mission_status():

    print("\n--- MISSION STATUS ---")

    warnings = check_sensor_limits()

    if warnings > 0:

        print("Mission Status: ATTENTION REQUIRED")

        print("Number of Warnings:", warnings)

    else:

        print("Mission Status: ALL SYSTEMS NORMAL")


# 8. GENERATE COMPLETE TELEMETRY REPORT

def generate_report():

    display_sensors()

    calculate_average()

    mission_status()

    print("\n================================")
    print("TELEMETRY REPORT COMPLETE")
    print("================================")


# 9. RUN PROGRAM

generate_report()


