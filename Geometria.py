def cuadrado():
    print('''
       * * * * * * * * *
       *               *
       *               *
       *               *
       *               *
       * * * * * * * * *      
''')

def triangulo():
        print('''

                    *
                   *  *
                  *     *
                 *        *
                * * * * * * *       
''')

user = input('''¿Que desea imprimir:

            1. Cuadrado
            2. Triángulo

''')



if user == '1':
      cuadrado()
    
else:
      triangulo()
                