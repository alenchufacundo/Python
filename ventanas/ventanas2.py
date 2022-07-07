from tkinter import Tk, messagebox, simpledialog
from datetime import date, datetime, timedelta

ventana = Tk()
ventana.withdraw ()
r = True
while r == True:
    fechastr = simpledialog.askstring(title="datos",prompt="ingrese una fecha: ") #Por que no es neceasrio el parent = window ? ->no es necesario aclarar, ya que automaticamente toma la del padre.
    fecha = datetime.strptime(fechastr,"%d/%m/%Y")
    dias = simpledialog.askinteger(title="Datos",prompt="ingrese una cantidad de dias: ")
    fechares = fecha + timedelta(days = dias)
    fechasrt2 = fechares.strftime("%d/&%m/%Y")
    messagebox.showinfo(title="Resultado",message=fechares)
    r = messagebox.askyesno(title="Terminar",message="desea volver a calcular?")

ventana.mainloop()