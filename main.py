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
