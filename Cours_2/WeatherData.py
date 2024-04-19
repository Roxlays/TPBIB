class TempDisplay:
    def update(self, temperature):
        print(f'Update temperature {temperature}')

class HumidityDisplay:
    def update(self, humidity):
        print(f'Update humidity {humidity}')

class PressureDisplay:
    def update(self, pressure):
        print(f'Update pressure {pressure}')


class WeatherData:

    def __init__(self):
        self.__tempDisplay = TempDisplay()
        self.__pressureDisplay = PressureDisplay()
        self.__humidityDisplay = HumidityDisplay()

    def get_temperature(self):
        # get data from sensor and return collected value
        return 12

    def get_pressure(self):
        # get data from sensor and return collected value
        return 900

    def get_humidity(self):
        # get data from sensor and return collected value
        return 70

    def measurements_changed(self):
        latest_temperature = self.get_temperature()
        latest_pressure = self.get_pressure()
        latest_humidity = self.get_humidity()

        self.__tempDisplay.update(latest_temperature)
        self.__pressureDisplay.update(latest_pressure)
        self.__humidityDisplay.update(latest_humidity)

if __name__ == '__main__':
    weatherData = WeatherData()
    for _ in range(2):
        weatherData.measurements_changed()
        