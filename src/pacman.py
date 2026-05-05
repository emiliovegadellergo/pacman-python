import pygame

class Pacman:
    def __init__(self):
        #posición
        self.x = 50
        self.y = 50
        #vida y puntos
        self.vidas = 3
        self.puntuacion = 0
        #movimiento
        self.velocidad = 2
        self.direccion = "der"
        #modo poder
        self.modoPoder = False
        self.tiempoPoder = 0


    #Métodos

    def estaVivo(self):
         if (self.vidas > 0):
             return True
        else:
            return False

    def perderVida(self):
        self.vidas -= 1
        #regresar al punto inicial
        self.x = 50
        self.y = 50
        self.direccion = "der"

    def activarPoder(self):
        self.modoPoder = True
        self.tiempoPoder = 300

    def actualizar_poder(self):
        if (self.modoPoder == True):
            self.tiempoPoder -= 1
            if (self.tiempoPoder <= 0):
                self.modoPoder = False

    def mover(self, tablero):
        if self.direccion == "der":
            self.x += self.velocidad
        elif self.direccion == "izq":
            self.x -= self.velocidad
        elif self.direccion == "arr":
            self.y -= self.velocidad
        elif self.direccion == "aba":
            self.y += self.velocidad

    def comer(self, punto):
        self.puntuacion += punto.valor
        if punto.esFruta:
            self.activarPoder()
        punto.desactivar()

    def dibujar(self, pantalla):
        pygame.draw.circle(pantalla, (255, 255, 0), (self.x, self.y), 15)


