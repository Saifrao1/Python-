import datetime as dt

aaj_kie_date = dt.datetime.now()

print(aaj_kie_date)

konsa_mahena = aaj_kie_date.month
print(konsa_mahena)

konsa_din = aaj_kie_date.day
print(konsa_din)

print(f"{aaj_kie_date:%B, %d, %Y}")


print(f"{aaj_kie_date:%a}")
print(f"{aaj_kie_date:%A}")

print(f"{aaj_kie_date:%B}")
print(f"{aaj_kie_date:%b}")

print(f"{aaj_kie_date:%Y}")
print(f"{aaj_kie_date:%y}")

print(f"{aaj_kie_date:%d}")
print(f"{aaj_kie_date:%w}")


print(f"{aaj_kie_date:%H}")
print(f"{aaj_kie_date:%I}")
print(f"{aaj_kie_date:%p}")
print(f"{aaj_kie_date:%M}")


print(f"{aaj_kie_date:%I} : {aaj_kie_date:%M} : {aaj_kie_date:%S}: {aaj_kie_date:%p}")


print(f"{aaj_kie_date:%j}")

print(f"{aaj_kie_date:%c}")
