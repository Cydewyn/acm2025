
transform broad_daylight:
    matrixcolor TintMatrix("#ffffff")

transform cloudy_daylight:
    matrixcolor TintMatrix("#c5c5c5")

transform overcast:
    matrixcolor TintMatrix("#555555")

transform dark:
    matrixcolor TintMatrix("#393939")

transform night:
    matrixcolor TintMatrix("#000000")

layeredimage beach_draft:
    if light == "broad_daylight":
        "images/backing_background.webp" at broad_daylight
    elif light == "cloudy_daylight":
        "images/backing_background.webp" at cloudy_daylight
    elif light == "overcast":
        "images/backing_background.webp" at overcast
    elif light == "dark":
        "images/backing_background.webp" at dark
    elif light == "night":
        "images/backing_background.webp" at night

    always:
        "images/beach_draft_no_background.png"
