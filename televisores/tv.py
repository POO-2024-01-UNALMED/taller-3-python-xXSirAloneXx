class TV():
    def __init__(self, marca, canal, precio, estado, volumen, control, numTV):
        self._marca = marca
        self._canal = canal
        self._precio = precio
        self._estado = estado
        self._volumen = volumen
        self._control = control

        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado

        self._numTV += 1

    
    def getMarca(self):
        return self._marca
    
    def setMarca(self, marca):
        self._marca = marca

    
    def getCanal(self):
        return self._canal
    
    def setCanal(self, canal):
        if(self._estado and canal >=1 and canal <= 120):
            self._canal = canal

    
    def getPrecio(self):
        return self._precio
    
    def setPrecio(self, precio):
        self._precio = precio
    

    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self, volumen):
        if(self._estado and volumen >= 0 and volumen <= 7):
            self._volumen = volumen


    def getControl(self):
        return self._control
    
    def setControl(self, control):
        self._control = control



    def setTurnOn(self):
        self.turnOn = True
    
    def setTurnOff(self):
        self.turnOff = False
    
    def getEstado(self):
        return self._estado
    


    def canalUp(self):
        self._canal += 1

    def canalDown(self):
        self._canal -= 1

        
    def volumenUp(self):
        self._volumen += 1
    def volumenDown(self):
        self._volumen -= 1