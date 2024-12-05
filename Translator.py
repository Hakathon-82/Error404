def calculate_ac_temperature(T_a, AT, adjustment_factor):
    """
    Calculate the optimal AC temperature based on air temperature (T_a),
    apparent temperature (AT), and adjustment factor.
    """
    T_ao = T_a - (AT - T_a) * adjustment_factor
    return T_ao

def calculate_heater_temperature(T_a, AT, RH, T_comfort=14, adjustment_factor=0.5):
    """
    Calculate the optimal heater temperature based on air temperature (T_a),
    apparent temperature (AT), relative humidity (RH), and adjustment factor.
    """
    # Adjust the adjustment factor based on relative humidity
    adjustment_factor_adj = adjustment_factor * (1 + (RH - 50) / 100)
    
    # Calculate the optimal heater temperature
    T_heater = T_a + (T_comfort - AT) * adjustment_factor_adj
    
    return T_heater

def should_open_windows(wind_speed, air_temp, relative_humidity, apparent_temp, ac_on, adjustment_factor):
    """
    Determines whether the windows should be opened or closed based on weather conditions and AC status.
    """
    # Thresholds for decision making
    wind_speed_threshold = 20  # km/h, above which windows should be closed
    comfortable_temp_range = (20, 25)  # Comfortable air temperature range (°C)
    high_humidity_threshold = 60  # % humidity, above which we might want to close windows
    high_apparent_temp_threshold = 30  # Apparent temperature above which windows should be closed

    # If AC is ON, close the windows
    if ac_on:
        return "Close the windows (AC is ON)"

    # Check if wind speed is too high
    if wind_speed > wind_speed_threshold:
        return "Close the windows (wind speed too high)"

    # Check if the apparent temperature is too high (due to humidity)
    if apparent_temp > high_apparent_temp_threshold:
        return "Close the windows (high apparent temperature)"

    # Check if the relative humidity is too high
    if relative_humidity > high_humidity_threshold:
        return "Close the windows (high humidity)"

    # Check if the air temperature is comfortable
    if comfortable_temp_range[0] <= air_temp <= comfortable_temp_range[1]:
        return "Open the windows (comfortable air temperature)"
    
    # If none of the conditions are satisfied, close the windows
    return "Close the windows (temperature not optimal)"

def main():
    # Input values
    wind_speed = float(input("Enter the wind speed (km/h): "))
    air_temp = float(input("Enter the air temperature (°C): "))
    relative_humidity = float(input("Enter the relative humidity (%): "))
    apparent_temp = float(input("Enter the apparent temperature (°C): "))
    adjustment_factor = float(input("Enter the adjustment factor (0.2 to 0.5): "))

    # Check if AC should be on
    if apparent_temp > 24:
        ac_on = True
        adjustment_factor = 0.5  # If AC is on, set adjustment factor to 0.5
        print("The AC is ON.")
    else:
        ac_on = False
        print("The AC is OFF.")
    
    # If the apparent temperature is below 8°C and the comfortable temperature is 14°C, turn on the heater
    if apparent_temp < 8:
        heater_on = True
        print("The heater is ON.")
        T_heater = calculate_heater_temperature(air_temp, apparent_temp, relative_humidity, T_comfort=14, adjustment_factor=0.5)
        print(f"The optimal heater temperature is: {T_heater:.2f}°C")
    else:
        heater_on = False
        print("The heater is OFF.")
    
    # Calculate the optimal AC temperature if AC is on
    if ac_on:
        T_ao = calculate_ac_temperature(air_temp, apparent_temp, adjustment_factor)
        print(f"The optimal AC temperature is: {T_ao:.2f}°C")
    
    # Check if windows should be open or closed
    window_status = should_open_windows(wind_speed, air_temp, relative_humidity, apparent_temp, ac_on, adjustment_factor)
    print(window_status)

# Run the program
if __name__ == "__main__":
    main()
