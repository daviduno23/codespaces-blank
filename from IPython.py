from IPython.display import Image, display
import random

hero_images = {
    "Invoker": "https://avatars.cloudflare.steamstatic.com/30801a3f7be405fd9ced7b35320c34e08202eab7_full.jpg",
    "Zeus": "https://dotawallpapers.com/wallpaper/dota2hq.eu-dota-2-god-zeus-illustration-4005-1920x1080.jpg",
    "Papoy El Maestro Borracho": "https://www.101soundboards.com/storage/board_pictures/28060-meepo-dota-meepo-dota.jpg",
    "Makanaky": "https://ovejanegra.com.pe/wp-content/uploads/2023/03/Makanaky.jpg",
    "Patricio Parodi": "https://i.pinimg.com/736x/0b/df/74/0bdf7405672cca55975de5966f2a9b32.jpg",
    "Phantom Assasin": "https://cdn.inprnt.com/thumbs/bd/2c/bd2c43a6aca4044d9e8ffa71081726e8.jpg"
}

heroes = {
    "Invoker": {
        "vida": 100,
        "daño": 12,
        "def_fisica": 5,
        "def_magica": 5,
        "velocidad": 15,
        "curas": 2,
        "habilidades": {
            "SunStrike": {"tipo": "magico", "daño": 17, "usos": 4},
            "Meteorito del Caos": {"tipo": "magico", "daño": 15, "efecto": "quemadura2rondas", "usos": 3}
        }
    },
    "Zeus": {
        "vida": 100,
        "daño": 12,
        "def_fisica": 4,
        "def_magica": 4,
        "velocidad": 25,
        "curas": 2,
        "habilidades": {
            "Rayo": {"tipo": "magico", "daño": 15, "usos": 4},
            "Armadura del Raikage": {"tipo": "defensivo", "efecto": "buff_def", "usos": 99}
        }
    },
    "Papoy El Maestro Borracho": {
        "vida": 100,
        "daño": 15,
        "def_fisica": 3,
        "def_magica": 3,
        "velocidad": 20,
        "curas": 2,
        "habilidades": {
            "Barril de Chela": {"tipo": "fisico", "daño": int(15 + 0.3 * 15), "usos": 2},
            "Borrachera extrema": {"tipo": "defensivo", "efecto": "def_plus5_2rondas", "usos": 3},
            "Maroma Club": {"tipo": "magico", "daño": 20, "efecto": "desarme+quemadura5rondas", "usos": 1, "costo_vida": 10}
        }
    },
    "Patricio Parodi": {
        "vida": 100,
        "daño": 17,
        "def_fisica": 2,
        "def_magica": 2,
        "velocidad": 20,
        "curas": 2,
        "habilidades": {
            "Golpear a tu Mujer": {"tipo": "fisico", "daño": 20, "usos": 2},
            "Llorar de impotencia": {"tipo": "defensivo", "efecto": "escudo50_2rondas", "usos": 1}
        }
    },
    "Makanaky": {
        "vida": 100,
        "daño": 15,
        "def_fisica": 3,
        "def_magica": 3,
        "velocidad": 25,
        "curas": 2,
        "habilidades": {
            "Sacar locro": {"tipo": "magico", "daño": 5, "usos": 6},
            "Calatearse": {"tipo": "fisico", "daño": 20, "usos": 1}
        }
    },
    "Phantom Assasin": {
        "vida": 100,
        "daño": 19,
        "def_fisica": 3,
        "def_magica": 7,
        "velocidad": 30,
        "curas": 2,
        "habilidades": {
            "Daga sofocante": {"tipo": "magico", "daño": int(10 + 0.3 * 19), "usos": 3},
            "Inmaterial": {"tipo": "defensivo", "efecto": "ignora40", "usos": 1}
        },
        "pasiva": {
            "nombre": "Golpe de gracia",
            "efecto": "cada 2 golpes basicos inflige daño adicional del 40%"
        },
        "cont_ataques": 0
    }
}

print("\n✨ SELECCIÓN DE HÉROES ✨")
for i, h in enumerate(heroes):
    print(f"{i+1}. {h}")

while True:
    eleccion = input("\n👉 Elige tu héroe por número: ")
    if eleccion.isdigit() and 1 <= int(eleccion) <= len(heroes):
        heroe_nombre = list(heroes.keys())[int(eleccion)-1]
        jugador = heroes[heroe_nombre].copy()
        break
    else:
        print("❌ Opción inválida")

print(f"\nHas elegido a {heroe_nombre}! 🛡️")
display(Image(hero_images[heroe_nombre]))

enemigos = [k for k in heroes if k != heroe_nombre]
enemigo_nombre = random.choice(enemigos)
enemigo = heroes[enemigo_nombre].copy()
enemigo["nombre"] = enemigo_nombre
print(f"\n⚔️ Tu oponente será: {enemigo_nombre}")
display(Image(hero_images[enemigo_nombre]))

log = []

while jugador["vida"] > 0 and enemigo["vida"] > 0:
    print(f"\n❤️ {heroe_nombre}: {jugador['vida']}    💀 {enemigo_nombre}: {enemigo['vida']}")
    print("1. Ataque Básico\n2. Usar Habilidad")
    accion = input("Elige acción: ")

    if accion == "1":
        daño = max(5, jugador["daño"] - enemigo["def_fisica"])
        jugador["cont_ataques"] = jugador.get("cont_ataques", 0) + 1
        if heroe_nombre == "Phantom Assasin" and jugador["cont_ataques"] % 2 == 0:
            extra = int(0.4 * jugador["daño"])
            daño += extra
            print(f"💥 Pasiva Golpe de Gracia activada! +{extra} daño")
        enemigo["vida"] -= daño
        print(f"➡️ Hiciste {daño} de daño físico")
        log.append(f"{heroe_nombre} hizo {daño} daño físico")

    elif accion == "2":
        habilidades = jugador["habilidades"]
        print("\nHabilidades disponibles:")
        for i, (h, info) in enumerate(habilidades.items()):
            print(f"{i+1}. {h} ({info['usos']} usos restantes)")
        h_sel = int(input("Elige habilidad: ")) - 1
        if 0 <= h_sel < len(habilidades):
            nombre_hab = list(habilidades.keys())[h_sel]
            info = habilidades[nombre_hab]
            if info["usos"] > 0:
                info["usos"] -= 1
                if "daño" in info:
                    defensa = enemigo["def_magica"] if info["tipo"] == "magico" else enemigo["def_fisica"]
                    daño = max(5, info["daño"] - defensa)
                    enemigo["vida"] -= daño
                    print(f"🔥 {nombre_hab} hizo {daño} de daño")
                    log.append(f"{heroe_nombre} usó {nombre_hab} e hizo {daño} de daño")
                else:
                    print(f"🛡️ Usaste {nombre_hab}, efecto aplicado")
                    log.append(f"{heroe_nombre} activó {nombre_hab}")
            else:
                print("❌ No te quedan usos")

    if enemigo["vida"] <= 0:
        break

    daño_e = max(5, enemigo["daño"] - jugador["def_fisica"])
    jugador["vida"] -= daño_e
    print(f"👹 {enemigo_nombre} te hizo {daño_e} de daño")
    log.append(f"{enemigo_nombre} hizo {daño_e} de daño")

print("\n🏁 FIN DEL COMBATE")
if jugador["vida"] > 0:
    print("🎉 ¡Has ganado!")
else:
    print("💀 Fuiste derrotado...")

with open("dy_dota3_historial.txt", "w") as f:
    for linea in log:
        f.write(linea + "\n")

print("📁 Historial guardado en 'dy_dota3_historial.txt'")