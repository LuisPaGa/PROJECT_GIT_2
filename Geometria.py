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

def rectangulo():
    print('''
        * * * * * * * * * * * * * * * * * * 
        *                                 *
        *                                 *
        * * * * * * * * * * * * * * * * * *      
    
    
    ''')


user = input('''¿Que desea imprimir:

            1. Cuadrado
            2. Triángulo
            3. Rectángulo

''')



if user == '1':
      cuadrado()
    
elif user == '2':
      triangulo()

else:
      rectangulo()      
                