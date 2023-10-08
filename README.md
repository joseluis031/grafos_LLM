# grafos_LLM
Este es el link del repositorio: [GitHub](https://github.com/joseluis031/grafos_LLM)

Para este trabajo nos han pedido implementar y evaluar una solución para mejorar la precisión y relevancia de ChatGPT, utilizando grafos de conocimiento para proporcionar un contexto estructurado.

Hemos dado cono una manera de solucionar uno de los mayores fallos actuales que tiene ChatGPT actualmente, las respuestas fallidas o "alucinaciones". 

Primero hemos creado un grafo con la información "buena" que contiene palabras como "IA", "Automático" o "Chatbots. 

A continuación definimos la función corregir_respuesta que cogerá la frase incorrecta que simula una respuesta incorrecta que nos habría proporcionado ChatGPT, descompondrá la oración para comparar palabra a palabra si esta pertenece al grafo, de ser así no la modificará porque es información correcta, pero de no estar en el grafo se sustituirá por un ```<<CORREGIDO>>```.

Por último para comprobar que el código funciona hemos incluido un ejemplo para que nos corrija una frase.

El código propuesto es el siguiente:
```
import networkx as nx

# Inicializamos un grafo de conocimiento
grafo_conocimiento = nx.Graph()

# Agregamos nodos y conexiones relevantes al grafo
grafo_conocimiento.add_nodes_from(["IA", "Aprendizaje", "Automático", "Procesamiento", "Lenguaje", "Natural", "Chatbots"])
grafo_conocimiento.add_edges_from([("IA", "Aprendizaje"),
                                   ("Aprendizaje", "Automático"),
                                  ("IA", "Procesamiento"),
                                  ("Procesamiento","Lenguaje"),
                                  ("Lenguaje", "Natural"),
                                  ("Aprendizaje", "Automático"),
                                  ("Automático", "Chatbots"),
                                  ("Natural","Chatbots")])

# Función para corregir respuestas inexactas
def corregir_respuesta(respuesta, grafo_conocimiento):
    palabras = respuesta.split()
    palabras_corregidas = []
    for palabra in palabras:
        if palabra not in grafo_conocimiento:
            palabras_corregidas.append("<<CORREGIDO>>")
        else:
            palabras_corregidas.append(palabra)
    respuesta_corregida = ' '.join(palabras_corregidas)
    return respuesta_corregida

# Ejemplo de uso
respuesta_inexacta = "La IA y el Aprendizaje Automático son componentes clave de los Chatbots"
respuesta_corregida = corregir_respuesta(respuesta_inexacta, grafo_conocimiento)

print("Respuesta Original:", respuesta_inexacta)
print("Respuesta Corregida:", respuesta_corregida)
```

Y el output esperado sería:
```
Respuesta Original: La IA y el Aprendizaje Automático son componentes clave de los Chatbots
Respuesta Corregida: <<CORREGIDO>> IA <<CORREGIDO>> <<CORREGIDO>> Aprendizaje Automático <<CORREGIDO>> <<CORREGIDO>> <<CORREGIDO>> <<CORREGIDO>> <<CORREGIDO>> Chatbots
```

Como podemos observar ha cambiado todas las palabras de la oración que no estaban incluidas en el grafo por ```<<CORREGIDO>>```, por tanto damos por válido el código.

## Conclusiones

Hemos intentado mejorar las soluciones inexactas o incorrectas que proporciona ChatGPT, utilizando grafos de conocimiento en los que tenemos registradas las que serían las palabras correctas. Ahora usando la función corregir_respuesta conseguireríamos que una respuesta inexacta que nos ha proporcionado el chat fuese revisada palabra a palabra para que si estas no etuviesen dentro del grafo de conocimiento, fuesen editadas por las correctas que fuesen convenientes. En nuetro caso como no tenemos la misma cantidad de información que puede tener ChatGPT, las palabras incorrectas las cambiamos por un ```<<CORREGIDO>>```.
