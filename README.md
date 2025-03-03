# Repositorio de Práctica de Redes Neuronales

Este repositorio contiene una implementación sencilla de una red neuronal con fines de aprendizaje. El código está basado en el siguiente video tutorial:

[Create a Simple Neural Network in Python from Scratch](https://www.youtube.com/watch?v=kft1AJ9WVDk) 
por [Jonas Bostoen](https://www.youtube.com/@JonasBostoen)

## Descripción
El script implementa una red neuronal básica con una sola capa. Utiliza la función de activación sigmoidea y su derivada para el entrenamiento. La red se entrena con un pequeño conjunto de datos que contiene cuatro ejemplos de entrada y una única salida.

## Resumen del Código
- **Función de Activación:** Función sigmoidea
- **Algoritmo de Entrenamiento:** Descenso de Gradiente
- **Iteraciones:** 100,000
- **Inicialización Aleatoria:** Los pesos sinápticos se inicializan aleatoriamente

## Dependencias
- Python 3.x
- NumPy

## Cómo Ejecutarlo
1. Clona este repositorio:
   ```sh
   git clone https://github.com/BecerraIgnacio/SimpleNeuralNetwork.git
   ```
2. Accede a la carpeta del proyecto:
   ```sh
   cd SimpleNeuralNetwork
   ```
3. Instala las dependencias:
   ```sh
   pip install numpy
   ```
4. Ejecuta el script:
   ```sh
   python simple_neural_network.py
   ```

## Salida Esperada
El script imprimirá:
- Pesos sinápticos iniciales generados aleatoriamente
- Pesos sinápticos finales después del entrenamiento
- Salida de la red neuronal después del entrenamiento

## Licencia
Este proyecto es de carácter educativo y sigue un enfoque de aprendizaje abierto. Siéntete libre de modificar y experimentar con el código.

## Autor
Repositorio creado por **Becerra Ignacio** como un ejercicio de práctica en redes neuronales.

