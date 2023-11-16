function nmwall -a ssid -a zone
    command nmcli connection modify $ssid connection.zone $zone
end