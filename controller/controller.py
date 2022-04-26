from models.LinkedList import *

def registar_país_início(lista, nome_do_país):
    lista.insert_at_start(nome_do_país)
    return lista


def registar_país_final(lista, nome_do_país):
    lista.insert_at_end(nome_do_país)
    return lista


def registar_depois_outro_elemento(lista,país_registrado, nome_do_país):
    lista.insert_after_item(país_registrado, nome_do_país)
    return lista

def registar_antes_outro_elemento(lista,país_registrado, nome_do_país):
    lista.insert_before_item(país_registrado, nome_do_país)
    return lista

def registar_país_outro_índice(lista,índice, nome_do_país):
    lista.insert_at_index(índice, nome_do_país)
    return lista

def verificar_número_de_elementos(lista):
    lista.get_count()
    return lista    

def verificar_se_país_encontra_lista(lista, nome_do_país):
    lista.search_item(nome_do_país)
    return lista

def eliminar_primeiro_elemento(lista):
    lista.delete_at_start()
    return lista    

def eliminar_último_elemento(lista):
    lista.delete_at_end()
    return lista   

def eliminar_um_determinado_país_da_lista(lista, nome_do_país):
    lista.elete_element_by_value(nome_do_país)
    return lista           