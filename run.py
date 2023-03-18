import ui
import sys
import menu

if __name__ == "__main__":
    # Si se ejecuta con el argumento -t, se inicia el menú de pruebas
    # de lo contrario, se inicia la interfaz gráfica

    # Para ejecutar el menú de pruebas, ejecutar el archivo run.py con el argumento -t
    # python run.py -t
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        menu.iniciar()
    else:
        app = ui.MainWindow()
        app.mainloop()

