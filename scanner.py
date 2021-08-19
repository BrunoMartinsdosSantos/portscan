import nmap

scanner = nmap.PortScanner()

print("Seja bem vindo ao Scanner")

ip = input("Digite o IP ou HOST a ser varrido: ")
print("O IP/HOST informado foi: ", ip)
type(ip)

menu = input("""\n Escolha o tipo de varredura a ser realizada
                1 -> Varredura do Tipo SYN
                2 -> Varredura do Tipo UPD
                3 -> Varredura do Tipo Intensa 
                Digite a opção escolhida: """)

print("A opção escolhida foi: ", menu)

if menu == "1":
    print("Versão do NMAP: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print(" ")
    print("Portas abertas: ", scanner[ip]['tcp'].keys())
elif menu == 2:
    print("Versão do NMAP: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print(" ")
    print("Portas abertas: ", scanner[ip]['udp'].keys())
elif menu == 3:
    print("Versão do NMAP: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sC')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print(" ")
    print("Portas abertas: ", scanner[ip]['tcp'].keys())
else:
    print("Opção inválida!!!!!!!!!!")

print("Scanner FINALIZADO COM SUCESSO.")
print(" ")
print("****Keep Happy Hacking****")
print("****Keep Learning****")
    






