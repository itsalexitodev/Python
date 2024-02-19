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

# Solicitar al usuario la ruta del archivo que contiene el nombre de usuario
read -p "Ingrese la ruta del archivo que contiene el nombre de usuario: " user_file
if [ ! -f "$user_file" ]; then
    echo "¡Archivo de usuario no encontrado!"
    exit 1
fi

# Solicitar al usuario la ruta del archivo que contiene la contraseña
read -p "Ingrese la ruta del archivo que contiene la contraseña: " password_file
if [ ! -f "$password_file" ]; then
    echo "¡Archivo de contraseña no encontrado!"
    exit 1
fi

# Leer el nombre de usuario y la contraseña desde los archivos
username=$(<"$user_file")
password=$(<"$password_file")

# Verificar si se proporciona una dirección IP
if [ -z "$1" ]; then
    echo "Uso: $0 <rango-de-IP>"
    exit 1
fi

# Escanear hosts en la red especificada
echo "Escaneando hosts en la red $1..."
hosts=$(sudo arp-scan --localnet | grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}')

# Mostrar la tabla de resultados
echo "--------------------------------------------------"
echo "|   IP        |   Estado del Servicio SSH   |  Estado de Acceso   |"
echo "--------------------------------------------------"
for host in $hosts; do
    if check_ssh_service "$host"; then
        check_ssh_connection "$username" "$password" "$host" &
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