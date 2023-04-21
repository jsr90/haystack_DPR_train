# Haystack DPR Train

Este proyecto está basado en [Chatbot para refugiados](https://github.com/josuemzx/Chatbot-para-refugiados), llevado a cabo en el contexto de [Saturdays AI](https://saturdays.ai/).

El archivo "train_haystack.ipybn" contiene una hoja de ruta para entrenar un modelo de preguntas y respuestas gracias al archivo "data.json", en formato SQuAD y obtenido del proyecto original. Una vez entrenado, el modelo es capaz, gracias al retriever, de encontrar la respuesta a una pregunta dada en un conjunto de documentos.

También encontramos en el proyecto el archivo "json_split.py" que permite dividir el conjunto de datos original en entrenamiento, test y validación.
