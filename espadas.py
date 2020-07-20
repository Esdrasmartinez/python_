import time
class Craftear_espada:
    def __init__(self):
        pass
    def Craftear_espadaa(self,mineral ,cantidad_palos,swords_list):
        self.mineral = mineral
        if self.mineral in swords_list.keys():
            self._craftear_cuerpo(mineral)
            self._craftear_mango(cantidad_palos)
            self._juntar_mango_y_cuerpo() 
        else:
            raise ValueError('Mineral no encontrado')   
        
    def _craftear_cuerpo(self,mineral):
        print('            _________________________________')
        print(f'              Crafteando cuerpo con: {mineral}   ')

        time_s = 0.2
        print('+++')
        time.sleep(time_s)
        print('++++')
        time.sleep(time_s)
        print('++ ++')
        time.sleep(time_s)
        print(' ++ ++')
        time.sleep(time_s)
        print('  ++ ++')
        time.sleep(time_s)
        print('   ++ ++')
        time.sleep(time_s)
        print('    ++ ++')
        time.sleep(time_s)
        print('     ++ ++')
        time.sleep(time_s)
        print('      ++ ++')
        time.sleep(time_s)
        print('       ++ ++')
        time.sleep(time_s)
        print('        ++ ++')
        time.sleep(time_s)
        print('         ++ ++')
        time.sleep(time_s)
        print('          ++ ++')
        time.sleep(time_s)
        print('           ++ ++')
        time.sleep(time_s)
        print('            ++ ++')
        time.sleep(time_s)     
        print('             ++ ++')
        time.sleep(time_s)            
        print('              ++ ++')
        time.sleep(time_s)            
        print('               ++ ++')
        time.sleep(time_s)           
        print('                ++ ++')
        time.sleep(time_s)            
        print('                 ++ ++')
        time.sleep(time_s)            
        print('                  ++ ++')
        time.sleep(time_s)           
        print('                   +++')
        time.sleep(time_s)

          
        
    def _craftear_mango(self,cantidad_palos):
        if cantidad_palos == 1:
            
            print(f'           Realizando mango de la espada      ')
            time_s = 0.2
            print('                          *')
            time.sleep(time_s)
            print('                           **')
            time.sleep(time_s)
            print('                             ***')
            time.sleep(time_s)
            print('                              ***')
            time.sleep(time_s)
            print('                               ***')
            time.sleep(time_s)
            print('                              ****')
            time.sleep(time_s)
            print('                             ****')
            time.sleep(time_s)
            print('                            ****')
            time.sleep(time_s)
            print('                           ****')
            time.sleep(time_s)
            print('                          ****')
            time.sleep(time_s)
            print('                         ****')
            time.sleep(time_s)
            print('                       ****%%')
            time.sleep(time_s)
            print('                      ****%%%%')
            time.sleep(time_s)
            print('                     ****  %%%%')
            time.sleep(time_s)
            print('            *       ****    %%%%')
            time.sleep(time_s)
            print('             **    ****      %%%%')
            time.sleep(time_s)
            print('              *** ****        %%%%')
            time.sleep(time_s)
            print('               ******          %%%%')
            time.sleep(time_s)
            print('                ****            %%%%')
            time.sleep(time_s)
            print('                                 %%%$$$')
            time.sleep(time_s)
            print('                                  %$$$$$')
            time.sleep(time_s)
            print('                                  $$$$$$$')
            time.sleep(time_s)
            print('                                  $$$$$$$')
            time.sleep(time_s)
            print('                                   $$$$$')
            time.sleep(time_s)
            print('                                    $$$')  


           
        elif cantidad_palos > 1:
            sobrante = cantidad_palos - 1
            print(f'Realizando mango de la espada sobran {sobrante} de madera')
        
        else:
            print(f'{cantidad_palos} no es suficiente madera para craftear el mango')
    
    def _juntar_mango_y_cuerpo(self):
        print(f'                Juntando mango y cuerpo')
        time_s = 0.2
        print('+++')
        time.sleep(time_s)
        print('++++')
        time.sleep(time_s)
        print('++ ++')
        time.sleep(time_s)
        print(' ++ ++')
        time.sleep(time_s)
        print('  ++ ++')
        time.sleep(time_s)
        print('   ++ ++')
        time.sleep(time_s)
        print('    ++ ++')
        time.sleep(time_s)
        print('     ++ ++')
        time.sleep(time_s)
        print('      ++ ++')
        time.sleep(time_s)
        print('       ++ ++')
        time.sleep(time_s)
        print('        ++ ++')
        time.sleep(time_s)
        print('         ++ ++')
        time.sleep(time_s)
        print('          ++ ++             *')
        time.sleep(time_s)
        print('           ++ ++            **')
        time.sleep(time_s)
        print('            ++ ++            **')
        time.sleep(time_s)
        print('             ++ ++           ***')
        time.sleep(time_s)
        print('              ++ ++           ***')
        time.sleep(time_s)
        print('               ++ ++          ***')
        time.sleep(time_s)
        print('                ++ ++        ****')
        time.sleep(time_s)
        print('                 ++ ++      ****')
        time.sleep(time_s)
        print('                  ++ ++    ****')
        time.sleep(time_s)
        print('                   ++ ++  ****')
        time.sleep(time_s)
        print('                    ++ ++****')
        time.sleep(time_s)
        print('                     +++****')
        time.sleep(time_s)
        print('                      +****')
        time.sleep(time_s)
        print('                       ****%%')
        time.sleep(time_s)
        print('                      ****%%%%')
        time.sleep(time_s)
        print('                     ****  %%%%')
        time.sleep(time_s)
        print('            *       ****    %%%%')
        time.sleep(time_s)
        print('             **    ****      %%%%')
        time.sleep(time_s)
        print('              *** ****        %%%%')
        time.sleep(time_s)
        print('               ******          %%%%')
        time.sleep(time_s)
        print('                ****            %%%%')
        time.sleep(time_s)
        print('                                 %%%$$$')
        time.sleep(time_s)
        print('                                  %$$$$$')
        time.sleep(time_s)
        print('                                  $$$$$$$')
        time.sleep(time_s)
        print('                                  $$$$$$$')
        time.sleep(time_s)
        print('                                   $$$$$')
        time.sleep(time_s)
        print('                                    $$$')  

        print(f'                 Tu espada está lista!')
        print('          _________________________________')


class Espada:

    
    def __init__(self,id_sword):
        self._swords = None
        self.id_sword = id_sword
        
    @property
    def swords(self):
        return self._swords

    @swords.setter
    def swords(self,swords_list):
        if self.id_sword in swords_list.keys():
            print("""           
            __________________________
            ESTADÍSTICAS DE LA ESPADA
            __________________________""")
            print(f'                     Daño: {swords_list[self.id_sword][0]}')
            print(f'                     Usos: {swords_list[self.id_sword][1]}')
            print(f'               Critical Hit Damage: {swords_list[self.id_sword][2]}')




        else:
            #raise ValueError('El mineral ingresado no existe')
            print(f'El mineral {self.id_sword} no existe intenta de nuevo')
      



swords_list = {
'Diamante' : [7,1562,14],
'Hierro' : [6,251,12],
'Oro' : [4,33,8],
'Piedra' : [5,132,10],
'Madera' : [4,60,8]
}
 

mineral_espada = input('De que ore quieres las espada: ')

iniciar_espada_piedra = Craftear_espada()
iniciar_espada_piedra.Craftear_espadaa(mineral_espada,1,swords_list)

diamond_sword = Espada(mineral_espada)
diamond_sword.swords = swords_list
            


class Bloque:
    def __init__(self,name,typeblock,duration):

        self.name = name
        self.type = typeblock
        self.duration = duration
        self._slide = None

    def expandir_cosa(self,type_item):
        if type_item == 'Lava' or type_item == 'lava':
            self._slide = 5
            

        elif type_item == 'Agua' or type_item == 'agua':
            self._slide = 8

        elif type_item == 'Fuego' or  type_item == 'fuego':
            self._slide = 15
       





#_____________________________________________________________
#Nos permite verificar si una instancia es parte de una clase 
# print(isinstance(diamond_sword,Espada))
#_____________________________________________________________
    
