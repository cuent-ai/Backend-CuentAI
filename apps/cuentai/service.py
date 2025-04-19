from typing import List, Dict, Any


class CuentAIService:
     def AIFormatter(self, TextEntry: str) -> List[str]:
        # Simulación de la respuesta de la llamada a la api
        # Se supone que obtendremos un str y lo tenemos que castear a array
        # Tener en cuenta las reglas que seguimos a la hora del formateo

        response = """SACERDOTE.- Con oportunidad has hablado
            Precisamente éstos me están indicando por señas que Creonte se acerca
            * Entrance of Creon
            EDIPO.- ¡Oh soberano Apolo! ¡Ojalá viniera con suerte liberadora, del mismo modo que viene con rostro radiante!
            SACERDOTE.- Por lo que se puede adivinar, viene complacido
            En otro caso no vendría así, con la cabeza coronada de frondosas ramas de laurel
            EDIPO.- Pronto lo sabremos, pues ya está lo suficientemente cerca para que nos escuche
            ¡Oh príncipe, mi pariente, hijo de Meneceo!
            ¿Con qué respuesta del oráculo nos llegas?
            CREONTE.- Con una buena
            Afirmo que incluso las aflicciones, si llegan felizmente a término, todas pueden resultar bien
            EDIPO.- ¿Cuál es la respuesta?
            Por lo que acabas de decir, no estoy ni tranquilo ni tampoco preocupado
            CREONTE.- Si deseas oírlo estando éstos aquí cerca, estoy dispuesto a hablar y también, si lo deseas, a ir dentro
            EDIPO.- Habla ante todos, ya que por ellos sufro una aflicción mayor, incluso, que por mi propia vida
            CREONTE.- Diré las palabras que escuché de parte del dios
            El soberano Febo nos ordenó, claramente, arrojar de la región una mancilla que existe en esta tierra y no mantenerla para que llegue a ser irremediable
            EDIPO.- ¿Con qué expiación?
            ¿Cuál es la naturaleza de la desgracia?
            CREONTE.- Con el destierro o liberando un antiguo asesinato con otro, puesto que esta sangre es la que está sacudiendo la ciudad
            EDIPO.- ¿De qué hombre denuncia tal desdicha?
            CREONTE.- Teníamos nosotros, señor, en otro tiempo a Layo como soberano de esta tierra, antes de que tú rigieras rectamente esta ciudad
            EDIPO.- Lo sé por haberlo oído, pero nunca lo vi"""

        lines = [line.strip() for line in response.splitlines() if line.strip()]
        return lines

     def AudioOutput(self, formated: List[str]) :
         
         return

     def CuentAIFlow(self, TextEntry: str) -> dict[str, Any]:
        # TODO:
        formated = self.AIFormatter(TextEntry)         

        audio = self.AudioOutput()
        # Preguntar si quiere video

        # Hacer un for llamando a las apis

        return formated
