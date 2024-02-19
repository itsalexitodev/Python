#!/bin/bash

# Función para verificar si el servicio SSH está activo en un host dado
check_ssh_service() {
    nc -z -w5 "$1" 22
    if [ $? -eq 0 ]; then
        return 0  # Servicio SSH activo
    else
        return 1  # Servicio SSH no activo
    fi
}

# Función para intentar conectar por SSH y comprobar si es exitoso
check_ssh_connection() {
    expect -c "
        spawn ssh -o StrictHostKeyChecking=no $1@$3
        expect {
            \"Are you sure you want to continue connecting\" {
                send \"yes\r\"
                expect \"assword:\"
                send \"$2\r\"
                expect eof
            }
            \"assword:\" {
                send \"$2\r\"
                expect eof
            }
        }
    " &>/dev/null
    if [ $? -eq 0 ]; then
        echo -e "| $3 | Powned   |"
    else
        echo -e "| $3 | Not Powned |"
    fi
}

# Solicitar al usuario la interfaz de red deseada
read -p "Ingrese la interfaz de red deseada (por ejemplo, lo, eth0, tun0): " interface

# Verificar si se proporciona una dirección IP
if [ -z "$1" ]; then
    echo "Uso: $0 <rango-de-IP>"
    exit 1
fi

# Escanear hosts en la red especificada utilizando la interfaz proporcionada
echo "Escaneando hosts en la red $1 utilizando la interfaz $interface..."
hosts=$(sudo arp-scan --interface="$interface" --localnet | grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}')

# Mostrar la tabla de resultados
echo "--------------------------------------------------"
echo "|   IP        |   Estado del Servicio SSH   |  Estado de Acceso   |"
echo "--------------------------------------------------"
for host in $hosts; do
    if check_ssh_service "$host"; then
        check_ssh_connection "alumne" "alumnealumne" "$host" &
        if [ $? -eq 0 ]; then
            ssh_status="Activo"
        else
            ssh_status="No activo"
        fi
    else
        ssh_status="No disponible"
        echo -e "| $host | $ssh_status | SSH no disponible |"
    fi
done
wait
echo "--------------------------------------------------"