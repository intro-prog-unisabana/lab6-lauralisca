[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Vwucp4F-)
# Laboratorio 6

# Problema 1

Debes crear un archivo de Python llamado **`dict_concept.py`**.
Dentro de ese archivo, define una función llamada **`get_config()`** que:

* No reciba **ningún parámetro**.
* Retorne un **diccionario** con los siguientes pares clave-valor:

  * `"width"` → `480` (entero)
  * `"height"` → `480` (entero)
  * `"color_mode"` → `"dark"` (cadena de texto)
  * `"sensitivity"` → `0.4` (flotante)

# Problema 2

Dentro del archivo **`dict_store.py`**, define una función llamada **`temp_and_color()`** que:

* **Entrada:**

  * Acepta **un parámetro**: un diccionario (que puede o no contener las claves `"temp"` y `"color"`).

* **Salida:**

  * Retorna **dos valores** (como una tupla):

    1. El valor almacenado bajo la clave `"temp"` si existe, de lo contrario `None`.
    2. El valor almacenado bajo la clave `"color"` si existe, de lo contrario `None`.

## **Ejemplo de Uso**

```python
data = {"temp": 22.5, "color": "blue", "status": "ok"}
print(temp_and_color(data))  
# Salida: (22.5, 'blue')

data = {"status": "ok"}
print(temp_and_color(data))  
# Salida: (None, None)
```

# Problema 3

Dentro del archivo **`dict_func.py`**, define una función llamada **`employee_print()`** que:

* **Entrada:**

  * Recibe un parámetro: `employee_info` (un diccionario con información del empleado).

* **Comportamiento:**

  1. Siempre imprime el **nombre**, el **salario** y el **rol** del empleado en el siguiente formato:
  
      ```plaintext
      Name: <nombre>
      Salary: <salario>
      Role: <rol>
      ```

     * Si la clave no existe en el diccionario, imprime `"N/A"` en su lugar.
  2. Después de imprimir esas tres claves, imprime cualquier **par clave-valor restante** del diccionario (si los hay) en un formato similar al anterior.
  3. Si el diccionario solo contiene los tres datos base (o está vacío), imprime `"No other info!"` después de los datos base.

* **Salida:**

  * La función **no retorna nada**. Solo imprime.

* **Recordatorio de Pista:**

  * Usa una función de diccionario para eliminar temporalmente `"Name"`, `"Salary"` y `"Role"` antes de recorrer los elementos restantes.
  * **No** se te pedirá modificar el formato de los valores de los datos en esta pregunta (es decir, título, minúsculas, mayúsculas).

## **Ejemplos de Comportamiento**

**Caso 1: Diccionario vacío**

```plaintext
Name: N/A
Salary: N/A
Role: N/A
No other info!
```

**Caso 2: Diccionario con información adicional**

```python
employee_info = {
    "Name": "Diego",
    "Salary": 5000000,
    "Role": "Janitor",
    "Years at company": 9001,
    "Hours per week": 2
}
employee_print(employee_info)
```

Salida:

```plaintext
Name: Diego
Salary: 5000000
Role: Janitor
Years at company: 9001
Hours per week: 2
```

# Problema 4

Depuración de un Programa de Inventario para una Frutería

## Objetivo

Estás ayudando a una pequeña frutería a reparar su **programa de gestión de inventario**. El programa usa **diccionarios** para llevar el registro de cuántas frutas hay en existencia.

Sin embargo, el programa está roto — tiene **5 errores distintos**. Tu tarea es:

1. Leer el código con atención.
2. Encontrar los 5 errores.
3. Corregir el programa para que funcione correctamente.

---

## Código con Errores

El código ya está en `debugging.py`. 
El siguiente código en `debugging.py` es el que debe ser corregido, para completar el ejercicio de depuración:

```python3
def show_inventory(inventory):
    print("\nCurrent Inventory:")
    # ¿Es esta la forma correcta de iterar sobre el diccionario?
    for fruit, stock in inventory:
        print(f"{fruit}: {stock}")
    print()

def add_fruit(inventory):
    fruit = input("Enter the name of the new fruit: ").strip()
    if fruit in inventory.keys():
        print(f"{fruit} already exists!\n")
    else:
        stock = input(f"Enter stock for {fruit}: ")
        # Algo está mal con la sintaxis aquí...
        inventory[fruit] == int(stock)
        print(f"{fruit} added with stock {stock}.\n")

def update_stock(inventory):
    fruit = input("Enter the name of the fruit to update: ").strip()
    # ¿Es esta la forma correcta de iterar sobre el diccionario?
    if fruit in inventory.items():
        amount = input(f"Enter amount to add to {fruit}'s stock: ")
        # ¿Es esta operación válida?
        inventory[fruit] += amount
        print(f"{fruit} stock increased by {amount}.\n")
    else:
        print(f"{fruit} is not in inventory. Use option 2 to add it.\n")

def menu():
    print("Options:")
    print("1 - View inventory")
    print("2 - Add new fruit")
    print("3 - Update existing fruit stock")
    print("4 - Exit")

def run_program():
    # Puede haber un error de sintaxis aquí...
    inventory = {
        "apples": 10
        "bananas": 20
        "oranges": 15
    }
```

---

## Guía de Depuración: Algunas Pistas

- El programa está lleno de errores de sintaxis. Estos deberían ser bastante obvios.
- ¡Presta atención a los errores en los bucles! ¿El programa está usando `.items()`, `.values()` y `.keys()` correctamente para recorrer el diccionario?
- Los `TypeError` son la pesadilla de los programadores. Estate atento.
- Los errores simples seguirán apareciendo una y otra vez, incluso a medida que los conceptos de programación se vuelvan más complejos. Por lo tanto, **se espera que puedas manejar errores conocidos en nuevos contextos.**

> **Importante:** El programa con errores es interactivo. Ejecútalo, observa los fallos y errores, y luego corrige las funciones. El bucle principal (menú y manejo de entradas) **no tiene errores** — los 5 errores están dentro de las funciones auxiliares o en los datos iniciales.

---

## Entrada/Salida Esperada

A continuación se muestran algunas entradas y salidas de ejemplo que indican cómo debe comportarse el programa una vez corregido.

### Ejemplo 1 — ver inventario y salir

**El usuario escribe:**

```plaintext
1
4
```

**El programa imprime:**

```plaintext
Welcome to the Fruit Shop!

Options:
1 - View inventory
2 - Add new fruit
3 - Update existing fruit stock
4 - Exit
Enter option number: 1

Current Inventory:
apples: 10
bananas: 20
oranges: 15

Options:
1 - View inventory
2 - Add new fruit
3 - Update existing fruit stock
4 - Exit
Enter option number: 4
Goodbye!
```

### Ejemplo 2 — agregar una fruta, actualizar su existencia, ver inventario

**El usuario escribe:**

```plaintext
2
grapes
40
3
apples
5
1
4
```

**El programa imprime:**

```plaintext
Options:
1 - View inventory
2 - Add new fruit
3 - Update existing fruit stock
4 - Exit
Enter option number: 2
Enter the name of the new fruit: grapes
Enter stock for grapes: 40
grapes added with stock 40.

Options:
1 - View inventory
2 - Add new fruit
3 - Update existing fruit stock
4 - Exit
Enter option number: 3
Enter the name of the fruit to update: apples
Enter amount to add to apples's stock: 5
apples stock increased by 5.

Options:
1 - View inventory
2 - Add new fruit
3 - Update existing fruit stock
4 - Exit
Enter option number: 1

Current Inventory:
apples: 15
bananas: 20
oranges: 15
grapes: 40

Options:
1 - View inventory
2 - Add new fruit
3 - Update existing fruit stock
4 - Exit
Enter option number: 4
Goodbye!
```

# Problema 5

**Análisis de Calificaciones en una Clase de Programación**

En `overall.py`, crea un diccionario de diccionarios que representa las calificaciones de los estudiantes en una clase de programación para ingenieros.

**El objetivo es calcular el promedio de calificaciones en todas las tareas y para todos los estudiantes.**

Este es el formato del diccionario:
```python
my_dict = {
    "student_id1":{"assignment1":100, ...},
    ...
}
```

Tu tarea será programar las funciones `student_averages` y `assignment_averages`:
- `student_averages`
    - **Entrada:**
        - Un diccionario con el formato visto anteriormente.
    - **Salida:**
        - Un diccionario de estudiantes con el identificador del estudiante como *clave* y el promedio del estudiante como *valor*.
- `assignment_averages`
    - **Entrada:**
        - Un diccionario con el formato visto anteriormente.
    - **Salida:**
        - Un diccionario de tareas con el nombre de la tarea como *clave* y el promedio de calificaciones de esa tarea como *valor*.

**Pista:** ¡recuerda usar `.items()`, `.keys()`, `.values()`, etc. para ayudarte a resolver este problema!  
**Pista:** usa la función `round()` para redondear tus resultados finales.


> Importante
**¡Para tus cálculos, redondea al entero más cercano!**

## Ejemplo:

### Datos de Ejemplo

```python
students = {
  "s1": {"hw1": 80, "hw2": 90, "hw3": 100},
  "s2": {"hw1": 70, "hw2": 75, "hw3": 85},
  "s3": {"hw1": 95, "hw2": 85, "hw3": 90}
}
```

---

### Llamadas a las Funciones

```python
print(student_averages(students))
# Esperado:
# {'s1': 90, 's2': 77, 's3': 90}

print(assignment_averages(students))
# Esperado:
# {'hw1': 82, 'hw2': 83, 'hw3': 92}
```

# Problema 6: Gestión de Calificaciones de Estudiantes con Diccionarios

## **Descripción General**
En este problema, desarrollarás un modulo de Python y un programa principal para gestionar las calificaciones de los estudiantes usando diccionarios de Python. El programa permitirá a los usuarios:
- Agregar estudiantes y sus calificaciones
- Calcular promedios de calificaciones
- Imprimir información de calificaciones de los estudiantes

>**Importante:** Para las Partes I-IV, trabajarás **exclusivamente** en `grades_manager.py`.

---

## **Parte I: Inicializar un Diccionario de Calificaciones de Estudiantes**

### **Estructura del Diccionario `student_grades`**
Las funciones de tu programa trabajarán con un parámetro de diccionario llamado `student_grades`, que sigue este formato:
- **Claves**: Nombres de los estudiantes (cadenas de texto)
- **Valores**: Otro diccionario donde:
  - **Claves**: Nombres de las materias (cadenas de texto)
  - **Valores**: Calificaciones (flotantes)

Aquí hay un ejemplo de dicho diccionario:

```python
student_grades = {
    "Alice": {
        "Math": 90.5,
        "English": 85.0,
        "Science": 92.0
    },
    "Bob": {
        "Math": 78.0,
        "English": 82.5,
        "History": 88.0
    },
    "Charlie": {
        "Science": 95.0,
        "English": 89.5
    }
}
```

### **Implementar la Función `initialize_dict`**
**Parámetros:**
- `student_name` (cadena de texto): Nombre del estudiante
- `subject_grades` (diccionario): Un diccionario donde los nombres de las materias (cadenas de texto) se asocian a calificaciones (flotantes)

**Funcionalidad:**
- Retorna un diccionario con `student_name` como clave y `subject_grades` como valor.
  Nota: Esto es solo para un estudiante.

#### Ejemplo:

**Llamada a la Función:**
```python
result = initialize_dict("Alice", {"Math": 90.5, "English": 85.0, "Science": 92.0})
```

**Valor de Retorno:**
```python
{'Alice': {'Math': 90.5, 'English': 85.0, 'Science': 92.0}}
```

---

## Parte II: **Implementar la Función `add_student`**
**Parámetros:**
- `student_grades` (diccionario, opcional): Por defecto es un diccionario vacío si no se proporciona.

**Funcionalidad:**
1. Pedir al usuario que ingrese el nombre de un estudiante:
   ```plaintext
   Enter student name:
   ```
   Convertir el nombre a **formato de título** (capitalizar cada palabra).
2. Pedir continuamente al usuario que ingrese materias (cadenas de texto) y calificaciones (flotantes) hasta que escriba `exit` (sin distinción entre mayúsculas y minúsculas):
   - Formato del mensaje de entrada:
     ```plaintext
     Enter subject and grade (or 'exit' to finish):
     ```
   - Formato de entrada:
     ```plaintext
     <materia>,<calificación>
     ```
     Convertir las materias a formato de título.
3. Crear un nuevo par clave-valor con el nombre del estudiante y sus materias/calificaciones, agregarlo a `student_grades` e imprimir:
   ```plaintext
   Student <name> successfully added to the grades management system.
   ```
4. Retornar el diccionario `student_grades` actualizado.

### Ejemplo:

**Llamada a la Función:**
```python
student_data = {}
updated_data = add_student(student_data)
```

**Entrada Estándar:**
```plaintext
john doe  
Math,95  
Science,88.5  
exit  
```

**Salida Estándar:**
```plaintext
Enter student name:
Enter subject and grade (or 'exit' to finish):
Enter subject and grade (or 'exit' to finish):
Enter subject and grade (or 'exit' to finish):
Student John Doe successfully added to the grades management system.
```

**Valor de Retorno de la Función:**
```python
{
    'John Doe': {
        'Math': 95.0,
        'Science': 88.5
    }
}
```

---

## Parte III: Obtener Estudiantes

### **Implementar la Función `get_students`**
**Parámetros:**
- `student_grades` (diccionario)
- `keys` (lista de nombres de estudiantes)

**Funcionalidad:**
- Realizar una búsqueda **sin distinción entre mayúsculas y minúsculas** para cada estudiante en `keys`:
  - Si un estudiante **no se encuentra**, imprimir:
    ```plaintext
    <name> not found!
    ```
    con `<name>` en formato de título, y continuar con el siguiente estudiante en `keys`.

  Nota: Incluso si un estudiante no se encuentra, la función debe seguir retornando el diccionario con los estudiantes encontrados.

- Retornar un diccionario que contenga solo los estudiantes solicitados y sus calificaciones, con los nombres en formato de título.
- Si no se encuentra ningún estudiante, retornar un **diccionario vacío**.

### Ejemplos:

**Ejemplo 1:**

**Llamada a la Función:**
```python
student_grades = {
    'Alice': {'Math': 90.5, 'English': 85.0},
    'Bob': {'Science': 88.0, 'History': 92.0}
}

result = get_students(student_grades, ["Alice", "Charlie"])
```

**Salida Estándar:**
```plaintext
Charlie not found!
```

**Valor de Retorno:**
```python
{
    "Alice": {"Math": 90.5, "English": 85.0}
}
```

**Ejemplo 2:**

**Llamada a la Función:**
```python
student_grades = {
    "Alice": {"Math": 90.5, "English": 85.0},
    "Bob": {"Science": 88.0, "History": 92.0}
}
result = get_students(student_grades, ["alice", "BOB"])
```

**Valor de Retorno:**
```python
{
    'Alice': {'Math': 90.5, 'English': 85.0},
    'Bob': {'Science': 88.0, 'History': 92.0}
}
```

**Ejemplo 3:**

**Llamada a la Función:**
```python
student_grades = {
    "Alice": {"Math": 90.5, "English": 85.0},
    "Bob": {"Science": 88.0, "History": 92.0}
}

result = get_students(student_grades, ["David", "Charlie"])
```

**Salida Estándar:**
```plaintext
David not found!
Charlie not found!
```

**Valor de Retorno:**
```python
{}
```
---

## Parte IV: Mostrar Análisis de Calificaciones

### **Implementar la Función `avg_by_student`**
**Parámetros:**
- `student_grades` (diccionario)
- `keys` (lista opcional de nombres de estudiantes, por defecto es `None`)

**Funcionalidad:**
- Si `keys` **no se proporciona**, imprimir el promedio de calificaciones de todos los estudiantes (formateado a **1 decimal**):
  ```plaintext
  Alice: 65.0  
  Ben: 60.5  
  ```
- Si `keys` **se proporciona**, imprimir solo los estudiantes solicitados y sus promedios.
- Esta función no debe retornar nada.

> **Pista:** Ya has escrito una función que obtiene los datos del estudiante requeridos.

### Ejemplos:

**Ejemplo 1:**

**Llamada a la Función:**
```python
student_grades = {
    "Alice": {"Math": 70.0, "English": 60.0},
    "Ben": {"Science": 55.0, "History": 66.0},
    "Charlie": {"Math": 90.0, "Science": 85.0}
}

avg_by_student(student_grades)
```

**Salida Estándar:**
```plaintext
Alice: 65.0  
Ben: 60.5  
Charlie: 87.5  
```

**Ejemplo 2:**

**Llamada a la Función:**
```python
student_grades = {
    "Alice": {"Math": 70.0, "English": 60.0},
    "Ben": {"Science": 55.0, "History": 66.0},
    "Charlie": {"Math": 90.0, "Science": 85.0}
}
avg_by_student(student_grades, ["Alice", "Charlie", "David"]) 
```

**Salida Estándar:**
```plaintext
David not found!
Alice: 65.0  
Charlie: 87.5 
```

**Ejemplo 3:**

**Llamada a la Función:**
```python
student_grades = {
    "Alice": {"Math": 70.0, "English": 60.0},
    "Ben": {"Science": 55.0, "History": 66.0},
    "Charlie": {"Math": 90.0, "Science": 85.0}
}
avg_by_student(student_grades, ["alice", "BEN"])
```

**Salida Estándar:**
```plaintext
Alice: 65.0  
Ben: 60.5
```

**Ejemplo 4:**

**Llamada a la Función:**
```python
student_grades = {
    "Alice": {"Math": 70.0, "English": 60.0},
    "Ben": {"Science": 55.0, "History": 66.0},
    "Charlie": {"Math": 90.0, "Science": 85.0}
}

avg_by_student(student_grades, ["David", "Eve"])
```

**Salida Estándar:**
```plaintext
David not found!  
Eve not found!  
```

---

# Parte V: Implementación del Programa Completo

## Desarrollar el Programa Completo de Gestión de Calificaciones
- Escribirás tu programa principal en `main.py`.
- Usa una instrucción `import` para importar todas tus funciones desde `grades_manager.py` y poder usarlas en esta parte.

**Funcionalidad:**
1. Imprimir un mensaje de bienvenida:
   ```plaintext
   Welcome to the Student Grades Manager!
   ```
2. Mantener un diccionario `my_grades` a lo largo del programa.
   - **No uses** las palabras clave `global` ni `nonlocal`.

3. Mostrar el menú principal y pedir la entrada del usuario:
   ```plaintext
   Select an option:  
   1. Add a student   
   2. Print student grade averages
   3. Exit  
   ```

4. Manejar las selecciones del usuario:
   - **Opción 1:** Agregar un estudiante usando la función implementada anteriormente.
   - **Opción 2:** Preguntar al usuario:
     ```plaintext
     Select an option:  
     a. Display all students  
     b. Display selected students  
     ```
     - **Si elige 'a'**, mostrar los promedios de calificaciones de todos los estudiantes.
     - **Si elige 'b'**, pedir una lista de nombres de estudiantes separados por comas:
       ```plaintext
       Enter student names (comma-separated):
       ```
       y mostrar solo sus promedios.
       - Los valores separados por comas se ingresarán en el formato:
       ```plaintext
       <nombre1>,<nombre2>,<nombre3>,...<nombreN>
       ```
     - En caso contrario, imprimir:
       ```plaintext
       Invalid option selected!
       ```
       y volver al menú principal.
   - **Opción 3:** Salir del programa e imprimir:
     ```plaintext
     Goodbye!
     ```

5. Si se ingresa una opción inválida en el menú principal, imprimir:
   ```plaintext
   Invalid option selected!
   ```
   y volver a pedir al usuario que elija.
6. Volver a mostrar el menú al usuario después de cada operación hasta que elija la opción 3.

## Ejemplo de Entrada/Salida

### Ejemplo 1:

**Entrada:**
```plaintext
1
john doe
Math,95
Science,88.5
exit
2
a
2
c
2
b
Jane Doe,John Doe
5
3
```

**Salida:**
```plaintext
Welcome to the Student Grades Manager!

Select an option:  
1. Add a student  
2. Print student grade averages  
3. Exit  

Enter student name: 
Enter subject and grade (or 'exit' to finish):  
Enter subject and grade (or 'exit' to finish):  
Enter subject and grade (or 'exit' to finish):   
Student John Doe successfully added to the grades management system.

Select an option:  
1. Add a student  
2. Print student grade averages  
3. Exit 

Select an option:  
a. Display all students  
b. Display selected students

John Doe: 91.8  

Select an option:  
1. Add a student  
2. Print student grade averages  
3. Exit 

Select an option:  
a. Display all students  
b. Display selected students  

Invalid option selected!

Select an option:  
1. Add a student  
2. Print student grade averages  
3. Exit 

Select an option:  
a. Display all students  
b. Display selected students

Enter student names (comma-separated):

Jane Doe not found!  
John Doe: 91.8  

Select an option:  
1. Add a student  
2. Print student grade averages  
3. Exit 

Invalid option selected!

Select an option:  
1. Add a student  
2. Print student grade averages  
3. Exit 

Goodbye!
```

# Problema 7

Se te ha dado un script inicial (`debug_top_socorer.py`) **con errores** para **"TopScorerAnalyzer"**.  
El programa debe permitir al usuario ingresar el nombre de un jugador y su puntaje, almacenarlos en un **diccionario**, y finalmente reportar qué jugador tiene el **puntaje más alto**.

Tu trabajo es **depurar el código** para que cumpla con todos los requisitos y pase el autoevaluador. Hay **5 líneas** de código incorrectas.

---

## Requisitos

1. Comenzar con un diccionario vacío llamado `scores`.  
2. Pedir al usuario repetidamente **dentro de un bucle while**:  
   ```plaintext
   Enter player and score as 'name score' (or type 'stop' to finish):
   ```
3. **Si** el usuario escribe stop (en cualquier combinación de mayúsculas y minúsculas), salir del bucle.  
4. En caso contrario, dividir la entrada en `name` y `score`. Convertir `score` a **int** y agregarlo al diccionario con `name` como clave.  
   * Si el nombre ya existe en el diccionario, sumar el nuevo puntaje al puntaje existente.  
5. Después de que el bucle termine:  
   * **Si** no se ingresó ningún puntaje, imprimir:  
     ```plaintext
     No scores recorded.
     ```
   * **Si no**, encontrar al jugador con el **puntaje total más alto** e imprimir:  
     ```plaintext
     Top scorer: <name> with <score> points.
     ```
     donde `<name>` es el jugador y `<score>` es su puntaje total.

* **Nota:** `input()` retorna una **cadena de texto** — debes convertir los valores al tipo de dato correcto antes de hacer operaciones aritméticas.

El texto y los espacios deben coincidir exactamente.

---

## Ejemplo de Ejecución

### Entrada
```plaintext
Alice 10
Bob 12
Alice 8
stop
```

### Salida
```plaintext
Enter player and score as 'name score' (or type 'stop' to finish):
Enter player and score as 'name score' (or type 'stop' to finish):
Enter player and score as 'name score' (or type 'stop' to finish):
Enter player and score as 'name score' (or type 'stop' to finish):
Top scorer: Alice with 18 points.
```

# Problema 8: Monitoreo Industrial de Temperatura

Script: `industrial_temperature.py`

Estás diseñando un sistema de monitoreo de temperatura para una instalación industrial. El sistema almacena lecturas de temperatura de distintos sensores en un **diccionario**, donde las **claves** son los nombres de los sensores y los **valores** son las lecturas de temperatura en Celsius.

- Escribe una función de Python `trigger_alarm(temperatures, threshold)` que reciba un diccionario de lecturas de sensores y una temperatura límite. El límite tendrá un valor por defecto de 80.
- La función debe retornar una lista con los nombres de los sensores que hayan **superado estrictamente** el límite.
- Si ninguna temperatura ha superado el límite o el diccionario está vacío, retornar una lista vacía.

**Parámetros de Ejemplo:**

```python
temperatures = {
    "sensor_1": 85.5,
    "sensor_2": 90.2,
    "sensor_3": 78.8,
    "sensor_4": 92.3
}
threshold = 88
```

**Valor de Retorno Esperado:**
```python
['sensor_2', 'sensor_4']
```

---

## **Ejemplo 1 (Proporcionando ambos parámetros — diccionario de temperaturas y límite):**

```python
temperatures = {
    "sensor_1": 85.5,
    "sensor_2": 90.2,
    "sensor_3": 78.8,
    "sensor_4": 92.3
}
threshold = 88
```

**Llamada a la Función:**
```python
trigger_alarm(temperatures, threshold)
```

**Valor de Retorno Esperado:**
```python
['sensor_2', 'sensor_4']
```

## **Ejemplo 2 (Proporcionando solo el diccionario de temperaturas, usando el límite por defecto de 80):**

```python
temperatures = {
    "sensor_A": 79.0,
    "sensor_B": 81.2,
    "sensor_C": 75.4,
    "sensor_D": 85.7
}
```

**Llamada a la Función:**
```python
trigger_alarm(temperatures)
```

**Valor de Retorno Esperado:**
```python
['sensor_B', 'sensor_D']
```

# Problema 9
Completa acknowledgments.txt