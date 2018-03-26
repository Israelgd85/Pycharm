segundos_str = input("Por Favor, entre com o número de segundos que deseja converter:")

total_segs = int(segundos_str)
dias = total_segs // 86400
horas_rest = total_segs  % 86400
horas = horas_rest // 3600
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restatntes_final = segs_restantes % 60

print(dias,"dias," ,horas, "horas," ,minutos, "minutos e", segs_restatntes_final, "segundos.")
