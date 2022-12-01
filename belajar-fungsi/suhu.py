def conv_reamur(celcius):
    convert_reamur = 4 / 5 * celcius
    return convert_reamur

def conv_farenheit(celcius):
    convert_farenheit = 9 / 5 * celcius  + 32
    return convert_farenheit

def conv_kelvin(celcius):
    convert_kelvin = celcius + 273
    return convert_kelvin

print('++++++++++ PROGAM KONVERSI SUHU ++++++++++ \n')

temperature = int(input('Masukan Skala Celcius: '))
reamur = conv_reamur(temperature)
farenheit = conv_farenheit(temperature)
kelvin = conv_kelvin(temperature)

print("\n88Hasil Konversi Suhu ", temperature, "C adalah ",reamur, "Reamur")
print("Hasil Konversi Suhu ", temperature, "C adalah ",farenheit, "Farenheit")
print("Hasil Konversi Suhu ", temperature, "C adalah ",kelvin, "Kelvin")
print('++++++++++++++++++++++++++++++++++++++++++++')
