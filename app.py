from classes.calcipv4 import CalcIPv4

calci_pv4 = CalcIPv4(ip='192.168.0.1', prefixo=24)

print(f'IP: {calci_pv4.ip}')
print(f'Máscara: {calci_pv4.mascara}')
print(f'Rede: {calci_pv4.rede}')
print(f'Broadcast: {calci_pv4.prefixo}')
print(f'Prefixo: {calci_pv4.prefixo}')
print(f'Número de IPs da rede: {calci_pv4.numero_ips}')
