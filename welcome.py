# List practice
rsvp_list: list[str] = ["Enrico", "Yun"]


def add_rsvp(friend: str) -> None:
    """Mutate the list by appending a friend"""
    rsvp_list.append(friend)


add_rsvp("Isapellet")
print(rsvp_list)


def has_rsvped(friend: str) -> bool:
    """Return True if friend's name is in RSVP list"""
    i: int = 0  # Representing current index in list
    while i < len(rsvp_list):
        if friend == rsvp_list[i]:
            return True
        i += 1
    return False


print(has_rsvped("Isapellet"))


# Dictionary practice
ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}
ice_cream["vanilla"] += 110
ice_cream["mint"] = 3
print(ice_cream)

if "mint" in ice_cream:
    print(ice_cream["mint"])

ice_cream.pop("vanilla")
print(ice_cream)

"""CQ01"""
vend: dict[str, str] = {
    "A1": "Oreos",
    "A2": "Lays",
    "B1": "Coke",
    "B2": "7up",
}

for prod in vend:
    print(prod)

flavors: set[str] = {"Orange", "Cherry", "Lime"}


def buy(vm: dict[str, str]) -> str:
    for prod in vm:
        return prod
    return "Other"


print(buy(vm=vend))
