import numpy as np

class InterpolacionPolinomica:
    def __init__(self, x, y):
        """
        Inicializa la clase con los datos de entrada.
        :param x: Lista de valores x.
        :param y: Lista de valores y correspondientes a cada x.
        """
        self.x = np.array(x)
        self.y = np.array(y)
        self.n = len(x)
        self.polinomio = self._crear_polinomio()

    def _crear_polinomio(self):
        """
        Crea el polinomio interpolado utilizando el método de Lagrange.
        :return: Función que representa el polinomio interpolado.
        """
        def lagrange_pol(xp):
            suma = 0
            for i in range(self.n):
                term = self.y[i]
                for j in range(self.n):
                    if j != i:
                        term *= (xp - self.x[j]) / (self.x[i] - self.x[j])
                suma += term
            return suma
        return lagrange_pol

    def evaluar(self, xp):
        """
        Evalúa el polinomio interpolado en un punto dado.
        :param xp: Valor de x para evaluar el polinomio.
        :return: Valor del polinomio en xp.
        """
        return self.polinomio(xp)

    def __call__(self, xp):
        """
        Hace la clase callable, permitiendo que se evalúe directamente con el valor de x.
        :param xp: Valor de x para evaluar el polinomio.
        :return: Valor del polinomio en xp.
        """
        return self.evaluar(xp)

# Ejemplo de uso
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

polinomio = InterpolacionPolinomica(x, y)
print(polinomio(2.5))  # Evalúa el polinomio en x = 2.5
