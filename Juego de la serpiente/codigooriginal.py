#librerias 
import tkinter 
import random 


#codigo de la ventana 
ventana = tkinter.Tk()
ventana.title("Juego de la serpiente")
ventana.geometry("600x600")
ventana.configure(bg="#00FF00")
#canvas 
tablero = tkinter.Canvas(
    ventana,
    width=600,
    height=600,
    bg="#202A36" )

tablero.pack()
serpiente = tablero.create_rectangle(100,100,150,150, fill="green")
cuerpo = [serpiente]
crecer = False  

comida = tablero.create_rectangle(300,300,320,320, fill="red")
puntos = 0 
marcador = tablero.create_text(
            300 , 20,
            text = "puntos: 0",
            fill= "white",
            font=("arial", 16)  )
perdiste_bro = tablero.create_text(
    300, 250,
    text="perdiste_bro",
    fill="red",
    font=("Arial", 35, "bold"),
    state="hidden"
)
direccion = "Derecha"

def cambiar_direccion(evento):
    global direccion
    if evento.keysym == "Up":
        direccion = "Arriba"
    elif evento.keysym == "Down":
        direccion = "Abajo"
    elif evento.keysym == "Left":
        direccion = "Izquierda"
    elif evento.keysym == "Right":
        direccion = "Derecha"
def comprobar_comida():
    global crecer , puntos 
    posicion = tablero.coords(serpiente)
    objetos = tablero.find_overlapping(

            posicion[0],
            posicion[1],
            posicion[2],
            posicion[3]

    )
    if comida in objetos:
        crecer = True 
        puntos += 10
        tablero.itemconfig(marcador, text=f"puntos: {puntos}")
        x = random.randrange(0 , 581 , 10)
        y = random.randrange(0 , 581 , 10)


        
        tablero.coords(comida, x, y, x + 20, y + 20)


def comprobar_colision():
    posicion = tablero.coords(serpiente)


    x1 , y1 , x2 , y2 = posicion 

    if x1 < 0 or y1 < 0 or x2 > 600 or y2 > 600:
        return True

    return False

def reiniciar():
    global serpiente, cuerpo, crecer
    global comida, puntos, marcador, game_over, direccion

    tablero.delete("all")

    serpiente = tablero.create_rectangle(
        100, 100, 150, 150,
        fill="green"
    )

    cuerpo = [serpiente]
    crecer = False
    direccion = "Derecha"

    comida = tablero.create_rectangle(
        300, 300, 320, 320,
        fill="red"
    )

    puntos = 0

    marcador = tablero.create_text(
        300, 20,
        text="Puntos: 0",
        fill="white",
        font=("Arial", 16)
    )

    game_over = tablero.create_text(
        300, 250,
        text="GAME OVER",
        fill="red",
        font=("Arial", 35, "bold"),
        state="hidden"
    )

    mover_serpiente()


boton_reiniciar = tkinter.Button(
    ventana,
    text="REINICIAR",
    command=reiniciar,
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white"
)

boton_reiniciar = tkinter.Button(
    ventana,
    text="REINICIAR",
    command=reiniciar,
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white"
)

boton_reiniciar = tkinter.Button(
    ventana,
    text="REINICIAR",
    command=reiniciar,
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white"
)

boton_reiniciar.place(x=250, y=550)





















def mover_serpiente():
    global crecer 
    posiciones = [tablero.coords(segmento) for segmento in cuerpo]

    for i in range(len(cuerpo) - 1, 0, -1):
        tablero.coords(cuerpo[i], posiciones[i - 1])
    if crecer:
        x1, y1, x2, y2 = posiciones[-1]

        nuevo_segmento = tablero.create_rectangle(
            x1, y1, x2, y2,
            fill="green"
        )

        cuerpo.append(nuevo_segmento)
        crecer = False
    if direccion == "Derecha":
        tablero.move(serpiente, 10, 0)
    elif direccion == "Izquierda":
        tablero.move(serpiente, -10, 0)
    elif direccion == "Arriba":
        tablero.move(serpiente, 0, -10)
    elif direccion == "Abajo":
        tablero.move(serpiente, 0, 10)
    if comprobar_colision():
        tablero.itemconfig(perdiste_bro, state="normal")
        return
    
    comprobar_comida()

    ventana.after(200, mover_serpiente)


ventana.bind("<Key>", cambiar_direccion)
mover_serpiente()

ventana.mainloop()