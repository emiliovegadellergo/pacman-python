import pygame

class Pacman:
    def __init__(self):
        #Atributos de posición en el mapa
        self.x = 50
        self.y = 50
        #Atributos de vida y puntos
        self.vidas = 3
        self.puntuacion = 0
        #Atributos de movimiento
        self.velocidad = 2
        self.direccion = "der"
        #Atributos para modo poder
        self.modo_poder = False
        self.tiempo_poder = 0


    #Métodos para moverse, comer, perder vida, activar poder y dibujar

    def esta_vivo(self):
        return self.vidas > 0

    def perder_vida(self):
        self.vidas -= 1
        self.x = 50
        self.y = 50
        self.direccion = "der"

    def activar_poder(self):
        self.modo_poder = True
        self.tiempo_poder = 300

    def actualizar_poder(self):
        if self.modo_poder:
            self.tiempo_poder -= 1
            if self.tiempo_poder <= 0:
                self.modo_poder = False

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
        if punto.es_fruta:
            self.activar_poder()
        punto.desactivar()

    def dibujar(self, pantalla):
        pygame.draw.circle(pantalla, (255, 255, 0), (self.x, self.y), 15)


