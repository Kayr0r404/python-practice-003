def weather_graph():
    """
    This function draws a weather graph for four weeks.
    each week will be observing a specific attribute.
    WEEK 1: RAIN 🌧️ , WEEK 2: CLOUDS ☁️, WEEK 3: WIND 🍃, WEEK 4: SUN ☀️

    Returns:
        str: A string representation of the weather graph.

    i.e for RAIN: each character represents 10% of rain/attribute observed that day.
    0% - no character
    10% - 1 character
    20% - 2 characters
    ...

    Week 1: RAIN
    MON: 🌧️
    TUE: 🌧️🌧️🌧️🌧️🌧️
    WED: 🌧️🌧️🌧️
    THU: 🌧️🌧️🌧️🌧️
    FRI: 🌧️🌧️🌧️🌧️🌧️

    your task is to read data from a file 'weather.txt' and draw the graphs accordingly.
    """
    emojis = {"RAIN": "🌧️", "CLOUDS": "☁️", "WIND": "🍃", "SUN": "☀️"}

    data = load_weather_from_file("weather.txt")
    for i, (wheather, emoji) in enumerate(emojis.items()):
        print(f"\nweek {i + 1}: {wheather}")
        for day, percentage in data[i]:
            print(f"{day}: {(percentage//10)*emoji} ")


def load_weather_from_file(path: str) -> list[list[int]]:
    weekdays = ["MON", "TUE", "WED", "THU", "FRI"]
    result: list[list[int]] = []

    with open(path, "r") as f:
        content = f.read()
    blocks = content.strip().split("---")

    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        values = []

        for day in weekdays:
            for line in lines:
                if line.startswith(day):
                    values.append((day, int(line.split(":")[1])))
        if values:
            result.append(values)

    return result


if __name__ == "__main__":
    weather_graph()
