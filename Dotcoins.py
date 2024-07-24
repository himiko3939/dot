import requests
import time
from colorama import init, Fore, Style
import sys
import os

init(autoreset=True)

def print_welcome_message():
    print(r"""
          
██╗  ██╗██╗███╗   ███╗██╗██╗  ██╗ █████╗ 
██║  ██║██║████╗ ████║██║██║ ██╔╝██╔══██╗
███████║██║██╔████╔██║██║█████═╝ ██║  ██║
██╔══██║██║██║╚██╔╝██║██║██╔═██╗ ██║  ██║
██║  ██║██║██║ ╚═╝ ██║██║██║ ╚██╗╚█████╔╝
╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═╝ ╚════╝""")
    print(Fore.GREEN + Style.BRIGHT + "Dotcoin BOT")
    print(Fore.GREEN + Style.BRIGHT + "Modded By Himiko\n")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_credentials():
    try:
        with open('tokens.txt', 'r') as file:
            credentials_list = file.readlines()
        credentials = [cred.strip() for cred in credentials_list]
        return credentials
    except FileNotFoundError:
        print("File 'tokens.txt' tidak ditemukan. Pastikan file tersebut ada di direktori yang sama dengan script.")
        return []

def fetch_task_ids(apikey, authorization):
    url = 'https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/get_filtered_tasks'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'apikey': apikey,
        'authorization': f'Bearer {authorization}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'origin': 'https://dot.dapplab.xyz',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
        'x-client-info': 'postgrest-js/1.9.2',
        'x-telegram-user-id': '6726676206'
    }
    data = {'platform': 'ios', 'locale': 'en', 'is_premium': False}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        tasks = response.json()
        task_ids = [task['id'] for task in tasks]
        return task_ids
    else:
        print(f"Failed to fetch tasks, status code: {response.status_code}")
        return []

def upgrade_dtc_miner(apikey, authorization):
    url = 'https://api.dotcoin.bot/functions/v1/upgradeDTCMiner'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'apikey': apikey,
        'authorization': f'Bearer {authorization}',
        'cache-control': 'no-cache',
        'content-length': '0',
        'origin': 'https://dot.dapplab.xyz',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; M2012K11AG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6422.165 Mobile',
        'x-telegram-user-id': '6577110188'
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get('success', False):
            print(f"{Fore.GREEN+Style.BRIGHT}Berhasil upgrade DTC Miner")
        else:
            print(f"{Fore.RED+Style.BRIGHT}Gagal upgrade DTC Miner, code: {response_data.get('code')}")
    else:
        print(f"{Fore.RED+Style.BRIGHT}Gagal upgrade DTC Miner, status code: {response.status_code}")

def add_attempts(lvl, apikey, authorization, current_level):
    url = 'https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/add_attempts'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'apikey': apikey,
        'authorization': f'Bearer {authorization}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        'x-client-info': 'postgrest-js/1.9.2'
    }

    while True:
        print(f"\r{Fore.CYAN+Style.BRIGHT}[ Upgrade ] : Mencoba upgrade ke level {lvl}", end="", flush=True)
        sys.stdout.flush()
        try:
            data = {'lvl': lvl}
            response = requests.post(url, headers=headers, json=data)
            response_data = response.json()
            if lvl > current_level:
                return False
            if response_data.get('success', False):
                return True
            else:
                lvl += 1
        except Exception as e:
            sys.stdout.write(f"Error while adding attempts: {e}\n")

def auto_clear_task(apikey, authorization):
    task_ids = fetch_task_ids(apikey, authorization)
    base_url = 'https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/complete_task'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'apikey': apikey,
        'authorization': f'Bearer {authorization}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        'x-client-info': 'postgrest-js/1.9.2',
        'x-telegram-user-id': '7003565657'
    }
    for task_id in task_ids:
        data = {'task_id': task_id}
        response = requests.post(base_url, headers=headers, json=data)
        if response.status_code == 200:
            response_data = response.json()
            if response_data.get('success', False):
                print(f"{Fore.GREEN+Style.BRIGHT}Task ID {task_id} berhasil diselesaikan")
            else:
                print(f"{Fore.RED+Style.BRIGHT}Task ID {task_id} gagal diselesaikan, code: {response_data.get('code')}")
        else:
            print(f"{Fore.RED+Style.BRIGHT}Gagal menyelesaikan Task ID {task_id}, status code: {response.status_code}")

def save_coins(apikey, authorization):
    url = 'https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/claim_earnings'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'apikey': apikey,
        'authorization': f'Bearer {authorization}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        'x-client-info': 'postgrest-js/1.9.2'
    }
    data = {}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        print(response_data)
        if response_data.get('success', False):
            print(f"{Fore.GREEN+Style.BRIGHT}Berhasil menyimpan koin")
        else:
            print(f"{Fore.RED+Style.BRIGHT}Gagal menyimpan koin, code: {response_data.get('code')}")
    else:
        print(f"{Fore.RED+Style.BRIGHT}Gagal menyimpan koin, status code: {response.status_code}")

def auto_upgrade_daily_attempt(apikey, authorization):
    current_level = 1
    while True:
        try:
            user_input = input("Masukkan level yang ingin dicapai (atau 'q' untuk keluar): ")
            if user_input.lower() == 'q':
                break
            target_level = int(user_input)
            if target_level < current_level:
                print(f"Level harus lebih besar dari level saat ini ({current_level}).")
                continue
            if add_attempts(target_level, apikey, authorization, current_level):
                current_level = target_level
                print(f"Berhasil mencapai level {current_level}")
            else:
                print(f"Gagal mencapai level {target_level}")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

def restore_attempts(apikey, authorization):
    url = 'https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/restore_attempts'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'apikey': apikey,
        'authorization': f'Bearer {authorization}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        'x-client-info': 'postgrest-js/1.9.2',
        'x-telegram-user-id': '7003565657'
    }
    data = {}
    false_count = 0
    while true:
        try:
            response = requests.post(url, headers=headers, json=data)
            response_data = response.json()
            if response.status_code == 200 and response_data.get('success', False):
                print(f"{Fore.GREEN+Style.BRIGHT}Berhasil restore attempts")
                return
            else:
                false_count += 1
                if false_count > 5:  # batas loop untuk menghindari infinite loop
                    print(f"{Fore.RED+Style.BRIGHT}Gagal restore attempts setelah beberapa kali percobaan")
                    return
                print(f"{Fore.RED+Style.BRIGHT}Gagal restore attempts, mencoba lagi... ({false_count})")
        except Exception as e:
            print(f"Error while restoring attempts: {e}")

def main():
    clear_console()
    print_welcome_message()

    credentials = load_credentials()
    if not credentials:
        return

    apikey, authorization = credentials

    while True:
        print("\n1. Upgrade DTC Miner")
        print("2. Auto Clear Task")
        print("3. Save Coins")
        print("4. Auto Upgrade Daily Attempt")
        print("5. Restore Attempts")
        print("6. Keluar")

        choice = input("Pilih opsi: ")
        if choice == '1':
            upgrade_dtc_miner(apikey, authorization)
        elif choice == '2':
            auto_clear_task(apikey, authorization)
        elif choice == '3':
            save_coins(apikey, authorization)
        elif choice == '4':
            auto_upgrade_daily_attempt(apikey, authorization)
        elif choice == '5':
            restore_attempts(apikey, authorization)
        elif choice == '6':
            break
        else:
            print("Opsi tidak valid, coba lagi.")

if __name__ == '__main__':
    main()
