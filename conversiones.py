import sys 
Peso_chileno=sys.argv[4]
Sol_peruano=sys.argv[1]
Peso_Argentinos=sys.argv[2] 
Dólar_Americano=sys.argv[3] 

print('Los ${sys.argv[4]} pesos equivalen a:')
print(f"{(float(sys.argv[4]))*(float(sys.argv[1]))} Soles")
print(f"{(float(sys.argv[4]))*(float(sys.argv[2]))}  Pesos Argetinos")
print(f"{(float(sys.argv[4]))*(float(sys.argv[3]))}  Dólares")
