import ipaddress

def subnetting_calculator():
    try:
        network_input = input("Masukkan jaringan (contoh: 192.168.1.0/24): ").strip()
        network = ipaddress.ip_network(network_input, strict=False)

        print(f"\nInformasi Jaringan untuk: {network_input}")
        print(f"Network Address    : {network.network_address}")
        print(f"Broadcast Address  : {network.broadcast_address}")
        print(f"Netmask            : {network.netmask}")
        print(f"Wildcard Mask      : {network.hostmask}")
        print(f"Jumlah total IP    : {network.num_addresses}")

        # Jumlah host = total IP - 2 (network + broadcast)
        usable_hosts = network.num_addresses - 2 if network.num_addresses > 2 else 0
        print(f"Jumlah Host yang bisa dipakai: {usable_hosts}")

        # Range IP host valid (network address + 1) sampai (broadcast address -1)
        if usable_hosts > 0:
            first_ip = list(network.hosts())[0]
            last_ip = list(network.hosts())[-1]
            print(f"Range IP Host Valid : {first_ip} - {last_ip}")
        else:
            print("Tidak ada host valid (network sangat kecil).")

    except ValueError:
        print("Input tidak valid! Pastikan formatnya benar (misal: 192.168.1.0/24)")

if __name__ == "__main__":
    subnetting_calculator()
