#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:24:29 2020

@author: pablo
"""

import numpy as np

class Nodo:
    
    def __init__(self, j1x, j1y, j2x, j2y, resultado, tablero):
        self.arriba = None
        self.abajo = None
        self.izquierda = None
        self.derecha = None
        self.tablero = tablero
        self.j1x = j1x
        self.j1y = j1y
        self.j2x = j2x
        self.j2y = j2y
        self.resultado = resultado

    def crearArbol(self, tipo, nivel):
        
        if nivel == 0:
            return 
        
        if tipo:
            if not self.arriba and self.j1y - 1 >= 0 and self.tablero[self.j1y - 1][self.j1x] != -1 and self.tablero[self.j1y - 1][self.j1x] != -2:
                
                tablero = np.copy(self.tablero)
                tablero[self.j1y - 1][self.j1x] = -1
                self.arriba = Nodo(self.j1x, self.j1y - 1, self.j2x, self.j2y, self.resultado + TABLERO[self.j1y - 1][self.j1x], tablero)
                self.arriba.crearArbol(not tipo, nivel - 1)
                
            if not self.derecha and self.j1x + 1 < len(TABLERO) and self.tablero[self.j1y][self.j1x + 1] != -1 and self.tablero[self.j1y][self.j1x + 1] != -2:
                
                tablero = np.copy(self.tablero)
                tablero[self.j1y][self.j1x + 1] = -1
                self.derecha = Nodo(self.j1x + 1, self.j1y, self.j2x, self.j2y, self.resultado + TABLERO[self.j1y][self.j1x + 1], tablero)
                self.derecha.crearArbol(not tipo, nivel - 1)
                
            if not self.abajo and self.j1y + 1 < len(TABLERO) and self.tablero[self.j1y + 1][self.j1x] != -1 and self.tablero[self.j1y + 1][self.j1x] != -2:
                
                tablero = np.copy(self.tablero)
                tablero[self.j1y + 1][self.j1x] = -1
                self.abajo = Nodo(self.j1x, self.j1y + 1, self.j2x, self.j2y, self.resultado + TABLERO[self.j1y + 1][self.j1x], tablero)
                self.abajo.crearArbol(not tipo, nivel - 1)
                
            if not self.izquierda and self.j1x - 1 >= 0 and self.tablero[self.j1y][self.j1x - 1] != -1 and self.tablero[self.j1y][self.j1x - 1] != -2:
      
                tablero = np.copy(self.tablero)
                tablero[self.j1y][self.j1x - 1] = -1
                self.izquierda = Nodo(self.j1x - 1, self.j1y, self.j2x, self.j2y, self.resultado + TABLERO[self.j1y][self.j1x - 1], tablero)
                self.izquierda.crearArbol(not tipo, nivel - 1)
        else:
            if not self.arriba and self.j2y - 1 >= 0 and self.tablero[self.j2y - 1][self.j2x] != -1 and self.tablero[self.j2y - 1][self.j2x] != -2:

                tablero = np.copy(self.tablero)
                tablero[self.j2y - 1][self.j2x] = -2
                self.arriba = Nodo(self.j1x, self.j1y, self.j2x, self.j2y - 1, self.resultado - TABLERO[self.j2y - 1][self.j2x], tablero)
                self.arriba.crearArbol(not tipo, nivel - 1)
                
            if not self.derecha and self.j2x + 1 < len(TABLERO) and self.tablero[self.j2y][self.j2x + 1] != -1 and self.tablero[self.j2y][self.j2x + 1] != -2:
                
                tablero = np.copy(self.tablero)
                tablero[self.j2y][self.j2x + 1] = -2 
                self.derecha = Nodo(self.j1x, self.j1y, self.j2x + 1, self.j2y, self.resultado - TABLERO[self.j2y][self.j2x + 1], tablero)
                self.derecha.crearArbol(not tipo, nivel - 1)
                
            if not self.abajo and self.j2y + 1 < len(TABLERO) and self.tablero[self.j2y + 1][self.j2x] != -1 and self.tablero[self.j2y + 1][self.j2x] != -2:
                
                tablero = np.copy(self.tablero)
                tablero[self.j2y + 1][self.j2x] = -2
                self.abajo = Nodo(self.j1x, self.j1y, self.j2x, self.j2y + 1, self.resultado - TABLERO[self.j2y + 1][self.j2x], tablero)
                self.abajo.crearArbol(not tipo, nivel - 1)
                
            if not self.izquierda and self.j2x - 1 >= 0 and self.tablero[self.j2y][self.j2x - 1] != -1 and self.tablero[self.j2y][self.j2x - 1] != -2:
                
                tablero = np.copy(self.tablero)
                tablero[self.j2y][self.j2x - 1] = -2
                self.izquierda = Nodo(self.j1x, self.j1y, self.j2x - 1, self.j2y, self.resultado - TABLERO[self.j2y][self.j2x - 1], tablero)
                self.izquierda.crearArbol(not tipo, nivel - 1)
    
    def imprimir(self):
        print('raiz ' + str(self.resultado))
        cola = list()
        cola.insert(0, (self, 0))
        i = 1
        
        while len(cola) != 0:
            actual = cola.pop()[0]
            
            if actual.arriba:
                print('arriba ' + str(i) + ' ' + str(actual.arriba.resultado))
                cola.insert(0, (actual.arriba, i))
                
            if actual.derecha:
                print('derecha ' + str(i) + ' ' + str(actual.derecha.resultado))
                cola.insert(0, (actual.derecha, i))
                
            if actual.abajo:
                print('abajo ' + str(i) + ' ' + str(actual.abajo.resultado))
                cola.insert(0, (actual.abajo, i))
                
            if actual.izquierda:
                print('izquierda ' + str(i) + ' ' + str(actual.izquierda.resultado))
                cola.insert(0, (actual.izquierda, i))
                
            i += 1
    
    def minimax(self, tipo = True, prof = 1, alfa = -1000, beta = 1000):
                
        if (not self.arriba and not self.derecha and not self.abajo and not self.izquierda) or prof == 0:
            return (self, '', alfa, beta)
        # elif self.arriba and not self.derecha and not self.abajo and not self.izquierda:
        #     return (self.arriba, 'arriba', alfa, beta)
        # elif not self.arriba and self.derecha and not self.abajo and not self.izquierda:
        #     return (self.derecha, 'derecha', alfa, beta)
        # elif not self.arriba and not self.derecha and self.abajo and not self.izquierda:
        #     return (self.abajo, 'abajo', alfa, beta)
        # elif not self.arriba and not self.derecha and not self.abajo and self.izquierda:
        #     return (self.izquierda, 'izquierda', alfa, beta)
        
        if tipo:
            
            maximo = None
            if self.arriba:
                arriba = self.arriba.minimax(not tipo, prof-1, alfa, beta)[0]
                alfa = max(alfa, arriba.resultado)
                
                if alfa >= beta:
                    return (arriba, 'arriba', alfa, beta)
                
                maximo = (arriba, 'arriba')
                
            if self.derecha:
                derecha = self.derecha.minimax(not tipo, prof-1, alfa, beta)[0]
                alfa = max(alfa, derecha.resultado)
                
                if alfa >= beta:
                    return (derecha, 'derecha', alfa, beta)
                
                if not maximo or derecha.resultado > maximo[0].resultado:
                    maximo = (derecha, 'derecha')
                
            if self.abajo:
                abajo = self.abajo.minimax(not tipo, prof-1, alfa, beta)[0]
                alfa = max(alfa, abajo.resultado)
                
                if alfa >= beta:
                    return (abajo, 'abajo', alfa, beta)
                
                if not maximo or abajo.resultado > maximo[0].resultado:
                    maximo = (abajo, 'abajo')
                
            if self.izquierda:
                izquierda = self.izquierda.minimax(not tipo, prof-1, alfa, beta)[0]
                alfa = max(alfa, izquierda.resultado)
                
                if alfa >= beta:
                    return (izquierda, 'izquierda', alfa, beta)
                
                if not maximo or izquierda.resultado > maximo[0].resultado:
                    maximo = (izquierda, 'izquierda')
            
            return (maximo[0], maximo[1], alfa, beta)
        
        else:
            
            minimo = None
            if self.arriba:
                arriba = self.arriba.minimax(not tipo, prof-1, alfa, beta)[0]
                beta = min(beta, arriba.resultado)
                
                if alfa >= beta:
                    return (arriba, 'arriba', alfa, beta)
                
                minimo = (arriba, 'arriba')
                
            if self.derecha:
                derecha = self.derecha.minimax(not tipo, prof-1, alfa, beta)[0]
                beta = min(beta, derecha.resultado)
                
                if alfa >= beta:
                    return (derecha, 'derecha', alfa, beta)
                
                if not minimo or derecha.resultado < minimo[0].resultado:
                    minimo = (derecha, 'derecha')
                
            if self.abajo:
                abajo = self.abajo.minimax(not tipo, prof-1, alfa, beta)[0]
                beta = min(beta, abajo.resultado)
                
                if alfa >= beta:
                    return (abajo, 'abajo', alfa, beta)
                
                if not minimo or abajo.resultado < minimo[0].resultado:
                    minimo = (abajo, 'abajo')
                
            if self.izquierda:
                izquierda = self.izquierda.minimax(not tipo, prof-1, alfa, beta)[0]
                beta = min(beta, izquierda.resultado)
                
                if alfa >= beta:
                    return (izquierda, 'izquierda', alfa, beta)
                
                if not minimo or izquierda.resultado < minimo[0].resultado:
                    minimo = (izquierda, 'izquierda')
            
            return (minimo[0], minimo[1], alfa, beta)
        
class Jugador:
    
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.tipo = tipo
    
    # def moverArriba(self):
    #     if (self.y - 1 >= 0 and tablero[self.y - 1][self.x] != -1 and tablero[self.y - 1][self.x] != -2)
    
    def puedeMover(self, tablero):
        
        if (
                (self.y - 1 >= 0 and tablero[self.y - 1][self.x] != -1 and tablero[self.y - 1][self.x] != -2) or 
                (self.x + 1 < len(TABLERO) and tablero[self.y][self.x + 1] != -1 and tablero[self.y][self.x + 1] != -2) or 
                (self.y + 1 < len(TABLERO) and tablero[self.y + 1][self.x] != -1 and tablero[self.y + 1][self.x] != -2) or 
                (self.x - 1 >= 0 and tablero[self.y][self.x - 1] != -1 and tablero[self.y][self.x - 1] != -2)
        ):
            return True
        
        return False
    
    def mueve(self, j2x, j2y, nivel, resultado, tablero):
        
        if self.tipo:
            raiz = Nodo(self.x, self.y, j2x, j2y, resultado, tablero)
            raiz.crearArbol(self.tipo, nivel)
            raiz.imprimir()
            movimiento = raiz.minimax(self.tipo, nivel)
            if movimiento[1] == 'arriba':
                self.y -= 1
                resultado += tablero[self.y][self.x]
                tablero[self.y][self.x] = -1
            elif movimiento[1] == 'derecha':
                self.x += 1
                resultado += tablero[self.y][self.x]
                tablero[self.y][self.x] = -1
            elif movimiento[1] == 'abajo':
                self.y += 1
                resultado += tablero[self.y][self.x]
                tablero[self.y][self.x] = -1
            elif movimiento[1] == 'izquierda': 
                self.x -= 1
                resultado += tablero[self.y][self.x]
                tablero[self.y][self.x] = -1
                
            return resultado
        else:
            while True:
                movimiento = input('Tu turno: ')
                if movimiento.lower() == 'w':
                    self.y -= 1
                    resultado -= tablero[self.y][self.x]
                    tablero[self.y][self.x] = -2
                    break
                elif movimiento.lower() == 'd':
                    self.x += 1
                    resultado -= tablero[self.y][self.x]
                    tablero[self.y][self.x] = -2
                    break
                elif movimiento.lower() == 's':
                    self.y += 1
                    resultado -= tablero[self.y][self.x]
                    tablero[self.y][self.x] = -2
                    break
                elif movimiento.lower() == 'a':
                    self.x -= 1
                    resultado -= tablero[self.y][self.x]
                    tablero[self.y][self.x] = -2
                    break
                else:
                    print('Movimiento invalido, intenta de nuevo.')
                
            return resultado

class Juego:
    
    def __init__(self):
        self.tablero = self.crearTablero()
        self.nivel = self.seleccionarNivel()
        self.resultado = self.tablero[0][0] - self.tablero[len(self.tablero) - 1][len(self.tablero) - 1]
        self.jugador1 = Jugador(0, 0, True)
        self.jugador2 = Jugador(len(self.tablero) - 1, len(self.tablero) - 1, False)

    def crearTablero(self):
        
        while True:
            
            N = int(input('Seleccione el tamaño del tablero (entre 4 y 10): '))
            
            if N >= 4 and N <= 10:     
                return np.random.randint(1, (2 * N) + 1, (N, N))
    
    def seleccionarNivel(self):
        
        while True:
            
            nivel = int(input('Seleccione el nivel de dificultad (minimo 3): '))
            
            if nivel >= 3:
                return nivel
    
    def imprimir(self):
        for f in range(len(TABLERO)):
            for c in range(len(TABLERO)):
                if f == self.jugador1.y and c == self.jugador1.x:
                    print('\u001b[44m{:3d}'.format(TABLERO[f][c]), end = ' ') #Imprime fondo azul
                    print('\u001b[0m', end = '')
                elif f == self.jugador2.y and c == self.jugador2.x:
                    print('\u001b[42m{:3d}'.format(TABLERO[f][c]), end = ' ') #Imprime fondo verde
                    print('\u001b[0m', end = '')
                elif self.tablero[f][c] == -1:
                    print('\u001b[34;1m{:3d}'.format(TABLERO[f][c]), end = ' ') #Imprime azul
                    print('\u001b[0m', end = '')
                elif self.tablero[f][c] == -2:
                    print('\u001b[32;1m{:3d}'.format(TABLERO[f][c]), end = ' ') #Imprime verde
                    print('\u001b[0m', end = '')
                else:
                    print('{:3d}'.format(TABLERO[f][c]), end = ' ')
            print()
    
    def jugar(self):
        
        self.tablero[self.jugador1.y][self.jugador1.x] = -1 
        self.tablero[self.jugador2.y][self.jugador2.x] = -2
        self.imprimir()
        print(self.resultado)
        
        while True:
            
            if not self.jugador1.puedeMover(self.tablero):
                break
            
            self.resultado = self.jugador1.mueve(self.jugador2.x, self.jugador2.y, self.nivel, self.resultado, self.tablero)
            
            self.imprimir()
            print(self.resultado)
            
            if not self.jugador2.puedeMover(self.tablero):
                break
        
            self.resultado = self.jugador2.mueve(self.jugador1.x, self.jugador1.y, self.nivel, self.resultado, self.tablero)
            
            self.imprimir()
            print(self.resultado)
        
        if self.resultado < 0:
            print('Ganaste: ' + str(self.resultado))
        elif self.resultado > 0:
            print('Gano la computadora: ' + str(self.resultado))
        else:
            print('Empate', str(self.resultado))
            
juego = Juego()
TABLERO = np.copy(juego.tablero)
juego.jugar()