# -*- coding: UTF-8 -*-
#class ConverteTemperaturaPython(object):
#    def converteCelsiusParaFahrenheit(temperaturaCelsius):
#        temperaturaFahrenheit = float(temperaturaCelsius) * 1.8 + 32;
#        return temperaturaFahrenheit;
#    def converteCelsiusParaKelvin(temperaturaCelsius):
#        temperaturaKelvin = float(temperaturaCelsius) + 273.15;
#        return temperaturaKelvin;
#    def converteFahrenheitParaCelsius(temperaturaFahrenheit):
#        temperaturaCelsius = (float(temperaturaFahrenheit) - 32)/1.8;
#        return temperaturaCelsius;
#    def converteFahrenheitParaKelvin(temperaturaFahrenheit):
#        temperaturaKelvin = (float(temperaturaFahrenheit) + 459.67)/1.8;
#        return temperaturaKelvin;
#    def converteKelvinParaCelsius(temperaturaKelvin):
#        temperaturaCelsius = float(temperaturaKelvin) - 273.15;
#        return temperaturaCelsius;
#    def converteKelvinParaFahrenheit(temperaturaKelvin):
#        temperaturaFahrenheit = float(temperaturaKelvin) * 1.8 - 459.67;
#        return temperaturaFahrenheit;

def converteCelsiusParaFahrenheit(temperaturaCelsius):
    temperaturaFahrenheit = float(temperaturaCelsius) * 1.8 + 32;
    return temperaturaFahrenheit;

def converteCelsiusParaKelvin(temperaturaCelsius):
    temperaturaKelvin = float(temperaturaCelsius) + 273.15;
    return temperaturaKelvin;

def converteFahrenheitParaCelsius(temperaturaFahrenheit):
    temperaturaCelsius = (float(temperaturaFahrenheit) - 32)/1.8;
    return temperaturaCelsius;

def converteFahrenheitParaKelvin(temperaturaFahrenheit):
    temperaturaKelvin = (float(temperaturaFahrenheit) + 459.67)/1.8;
    return temperaturaKelvin;

def converteKelvinParaCelsius(temperaturaKelvin):
    temperaturaCelsius = float(temperaturaKelvin) - 273.15;
    return temperaturaCelsius;

def converteKelvinParaFahrenheit(temperaturaKelvin):
    temperaturaFahrenheit = float(temperaturaKelvin) * 1.8 - 459.67;
    return temperaturaFahrenheit;

# print('Temperatura celsius para fahrenheit: ' + str(converteCelsiusParaFahrenheit(1)));
# print('Temperatura celsius para kelvin: ' + str(converteCelsiusParaKelvin(1)));
# print('Temperatura fahrenheit para celsius: ' + str(converteFahrenheitParaCelsius(1)));
# print('Temperatura fahrenheit para kelvin: ' + str(converteFahrenheitParaKelvin(1)));
# print('Temperatura kelvin para celsius: ' + str(converteKelvinParaCelsius(1)));
# print('Temperatura kelvin para fahrenheit: ' + str(converteKelvinParaFahrenheit(1)));