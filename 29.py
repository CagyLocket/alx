chleb = 6.50
sok = 4.00
paczek = 5.50

chlebow = int(input("Ile kupujesz chleba? "))
sokow = int(input("Ile kupujesz soków? "))
paczkow = int(input("Ile kupujesz pączków? "))

razem_chleb = chleb * chlebow
razem_sok = sok * sokow
razem_paczek = paczek * paczkow
razem_do_zaplaty = float(razem_chleb + razem_sok + razem_paczek)

# print(f"Twoje zamówienie to:")
# print(f"1. Chlebów - {chlebow}szt. - razem: {razem_chleb}")
# print(f"2. Soków - {sokow}szt. - razem: {razem_sok}")
# print(f"3. Pączków - {paczkow}szt. - razem: {razem_paczek}")
# print(f"Razem do zapłaty: {razem_do_zaplaty}")

print(f"Twoje zamówienie to:\n "
      f"1. Chlebów - {chlebow}szt. - razem: {razem_chleb}\n"
      f"2. Soków - {sokow}szt. - razem: {razem_sok}\n "
      f"3. Pączków - {paczkow}szt. - razem: {razem_paczek}\n"
      f"Razem do zapłaty: {razem_do_zaplaty}")

