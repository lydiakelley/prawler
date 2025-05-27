def sample():
    
    # import libraries
    import urtc
    import ms5803
    import tsl2561

    from machine import I2C, Pin

    i2c = I2C(scl = Pin(5), sda = Pin(4))
    print(i2c.scan())

    datafile = open("wirewalkerdata.csv", "a")
   
    # REAL TIME CLOCK 
    rtc = urtc.DS3231(i2c)
    d = rtc.datetime()
    date = str(d.year) + '/' + str(d.month) + '/' + str(d.day) + ' ' + str(d.hour) + ':' + str(d.minute)
    print(date)

    # WATER PRESSURE & TEMPERATURE
    water_pressure = ms5803.read(i2c=i2c, address = 118)
    print(water_pressure)
    pressure = (water_pressure[0])
    print(pressure)
    temperature = (water_pressure[1])
    print(temperature)

    # LIGHT SENSOR
    sensor = tsl2561.TSL2561(i2c)
    light = sensor.read()
    print(light)
    
    data_line = str(str(date) + ',' + str(temperature) + ',' + str(pressure) + ',' + str(light) + '\n')
    
    datafile.write(data_line)
     
    datafile.close()
    
    
# SAMPLING FUNCTION FUTURE

#    # VARIABLES
#     current_depth = 0.0
#     last_depth = 0.0
#     last_measurement = 0
# 
#     # SAMPLING REQUIREMENTS
#     if current_depth != last_depth :
#             datafile.write(date, depth, temperature, light)
#             last_measurement = time_seconds
#             last_depth = depth
#             
#     elif current_depth == last_depth and last_measurement - time_seconds >= 1800:
#             datafile.write(date, depth, temperature, light)
#             last_measurement = time_seconds
#             last_depth = depth
