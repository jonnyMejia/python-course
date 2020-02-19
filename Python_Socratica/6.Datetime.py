import datetime 

""" ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', 
'__doc__','__file__', '__loader__', '__name__', '__package__', 
'__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 
'time', 'timedelta', 'timezone', 'tzinfo'] """
print(dir(datetime))

my_birthday=datetime.date(2001,6,5)
# 2001-06-05
# yyyy-mm-dd
print(my_birthday)

# 2001
print(my_birthday.year)
# 6
print(my_birthday.month)
# 5
print(my_birthday.day)

# FORMATO FECHA Y HORA
""" 
% A : Nombre del dia completo
% a : Nombre del dia abreviado
% B : Nombre del mes completo
% b : Nombre del mes abreviado
% Y : Año 4 digitos 
% y : Año 2 digitos 
% d : Dia del mes con un padded con cero (01-31)
% m : mes como numero (01-12)
% H : Hora formato de 24 (00-23)
% I : Hora formato de 12 (00-12)
% p : AM o PM
% M : Minutos (00-59)
% S : Segundos (00-59)
% f : Microsegundos
 """
# Tuesday, June 05, 2001
print(my_birthday.strftime("%A, %B %d, %Y"))

message = "I was born on {:%A, %B %d, %Y}."
# I was born on Tuesday, June 05, 2001.
print(message.format(my_birthday))

launch_datetime = datetime.datetime(2017,3,20,22,27,0)
# 2017-03-20 22:27:00
print(launch_datetime)

ahora = datetime.datetime.now
# Se imprime con los microsegundos
print(ahora)

# PARSE DE FECHAS Y HORAS
moon_landing = input("Ingresa la fecha de la luna '7/20/1969' \n")
moon_landing_datetime = datetime.datetime.strptime(moon_landing,"%m/%d/%Y")

# 1969-07-20 00:00:00
print(moon_landing_datetime)



