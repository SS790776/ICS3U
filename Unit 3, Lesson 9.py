def wc(TdegC, windKPH):
   """
    * Calculates the wind chill, given
    * TdegC: the temp in degrees C
    * windKPH: the wind speed in km/h
    *
    * Returns:
    * vTemp: Wind chill in degrees C
   """
   vTemp = 0
   
   vTemp = 13.12 + 0.6215 *TdegC
   vTemp -= 11.37 * (windKPH**0.16)
   vTemp += 0.3965 * TdegC * (windKPH**0.16)

   return vTemp

print("Windchill calculator")
print("------------------------------------")
T = -5.0
W = 10.0
print("WC=%8.3f T=%8.3f W=%6.3f km/h" % (wc(T, W), T, W))
print("There is Low Risk.\n")
T = -20.0
W = 20.0
print("WC=%8.3f T=%8.3f W=%6.3f km/h" % (wc(T, W), T, W))
print("There is a high risk of frostbite, please stay indoors and keep warm \n")
T = -45.0
W = 40.0
print("WC=%8.3f T=%8.3f W=%6.3f km/h" % (wc(T, W), T, W))
print("Extreme risk: exposed skin freezes in under 2 minutes. Please stay indoors and keep warm \n")
