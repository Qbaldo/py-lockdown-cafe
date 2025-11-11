from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: str) -> str:
    masks_count = 0
    for friend in friends:

        try:
            cafe.visit_cafe(friend)

        except VaccineError :
            return "All friends should be vaccinated"

        except NotWearingMaskError :
            masks_count += 1

    if not masks_count:
        return f"Friends can go to {cafe.name}"
    else:
        return f"Friends should buy {masks_count} masks"
