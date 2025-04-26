import sys
from modeloparcial import compras, eventos  # Asegurate de que este archivo exista y tenga las listas

if len(sys.argv) < 2:
    print("Por favor, ingresá un tipo de evento como parámetro")
    sys.exit(1)

tipo_buscado = sys.argv[1]
total_recaudado = 0
encontrado = False

# Buscar los nombres de eventos que coincidan con el tipo
eventos_filtrados = [e.nombre_evento for e in eventos if e.tipo== tipo_buscado]

# Mostrar compras correspondientes a esos eventos
for compra in compras:
    if compra.nombre_evento in eventos_filtrados:
        print(f"Evento: {compra.nombre_evento} - Cliente: {compra.nombre_cliente} - Entradas: {compra.cantidad_entradas} - Total: ${compra.monto_total}")
        total_recaudado += compra.monto_total
        encontrado = True

if not encontrado:
    print(f"No se encontraron compras para eventos del tipo '{tipo_buscado}'.")
else:
    print(f"\nTotal recaudado para eventos tipo '{tipo_buscado}': ${total_recaudado}")
