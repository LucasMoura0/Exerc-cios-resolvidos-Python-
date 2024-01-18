try:
    x = int(input('Primeiro Valor?'))
    y = int(input('Segundo Valor?'))
    z = x / y

except ValueError:
    print('Exceção: Entrada Inválida')
except ZeroDivisionError:
    print('Exceção: Divisão por Zero!')
except:
    print('Ocorreu uma Exceção!')
else:
    print('O resultado da divisão é:', z)

