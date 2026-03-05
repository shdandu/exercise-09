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
