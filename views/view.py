from configparser import ParsingError
import controller.controller as cl
from models.LinkedList import LinkedList
def main ():

    lista = LinkedList()

    while True:

        comando = input().upper().split()

        if comando[0] == "RPI":
            nome_do_país = comando[1]
            registar_país_início(lista, nome_do_país)

        if comando[0] == "RPF":    
            nome_do_país = comando[1]
            registar_país_final(lista, nome_do_país)

        if comando[0] == "RPDE":
            nome_do_país = comando[1]
            país_registrado = comando[2]
            registar_depois_outro_elemento(lista, país_registrado, nome_do_país)  

        if comando[0] == "RPAE":
            nome_do_país = comando[1]
            país_registrado = comando[2]
            registar_antes_outro_elemento(lista, país_registrado,nome_do_país)  

        if comando[0] == "RPII":
            nome_do_país = comando[1]
            índice = int(comando[2]) 
            registar_país_outro_índice(lista,índice, nome_do_país)  
    
        if comando[0] == "VNE":
            verificar_número_de_elementos(lista)   

        if comando[0] == "VP":
            nome_do_país = comando[1]
            verificar_se_país_encontra_lista(lista, nome_do_país)    

        if comando[0] == "EPE":
            eliminar_primeiro_elemento(lista)    

        if comando[0] == "EUE":
            eliminar_último_elemento(lista)    

        if comando[0] == "EP":
            nome_do_país = comando[1]
            eliminar_um_determinado_país_da_lista(lista, nome_do_país)    
                           

def registar_país_início(lista, nome_do_país):
    cl.registar_país_início(lista, nome_do_país)
    lista.traverse_list()

def registar_país_final(lista, nome_do_país):
    cl.registar_país_final(lista, nome_do_país)
    lista.traverse_list()    

def registar_depois_outro_elemento(lista,país_registrado, nome_do_país):
    cl.registar_depois_outro_elemento(lista,país_registrado, nome_do_país)
    lista.traverse_list()    

def registar_antes_outro_elemento(lista,país_registrado, nome_do_país):
    cl.registar_antes_outro_elemento(lista,país_registrado, nome_do_país)
    lista.traverse_list()        

def registar_país_outro_índice(lista,índice, nome_do_país):
    cl.registar_país_outro_índice(lista,índice, nome_do_país)
    lista.traverse_list()       

def verificar_número_de_elementos(lista):
   c = cl.verificar_número_de_elementos(lista)
   print(f"O numero de elementos são {c}")
         

def verificar_se_país_encontra_lista(lista, nome_do_país):
    if cl.verificar_se_país_encontra_lista(lista, nome_do_país) == False:
        print(f"O país {nome_do_país} não se encontra na lista")
    else: 
        print(f"O país {nome_do_país} encontra-se na lista")

       

def eliminar_primeiro_elemento(lista):
    nome_do_país = lista.start_node.item
    cl.eliminar_primeiro_elemento(lista)
    print(f"O país{nome_do_país} foi eliminado da lista ")      

def eliminar_último_elemento(lista):
    nome_do_país = lista.end_node.item
    cl.eliminar_último_elemento(lista)
    print(f"O país {nome_do_país} foi eliminado da lista. ")  

def eliminar_um_determinado_país_da_lista(lista, nome_do_país):
    if cl.verificar_se_país_encontra_lista(lista, nome_do_país) == False:
        print(f"O país {nome_do_país} não se encontra na lista")
    else:
       cl.eliminar_um_determinado_país_da_lista(lista, nome_do_país)
       print(f"O país {nome_do_país} foi eliminado com sucesso. ")         
