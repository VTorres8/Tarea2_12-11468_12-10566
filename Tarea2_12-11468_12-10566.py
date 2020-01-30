import unittest
from Persona import Persona
<<<<<<< HEAD

=======
>>>>>>> ce73cbda30803ba639dc262164452f63e94dfba8
class TestPension(unittest.TestCase):

    #Caso de Prueba para crear una instancia de la clase Persona
    def test_CrearPersona(self):
        persona = Persona()
        self.assertIsInstance(persona,Persona)
       