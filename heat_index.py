"""Calculate NWS Heat Index values for various temperature/humidity combinations."""


def heat_index(t: float, rh: float) -> float:
    """NWS Heat Index (Rothfusz regression). T in °F, RH in %."""
    hi = 0.5 * (t + 61.0 + ((t - 68.0) * 1.2) + (rh * 0.094))
    if hi >= 80:
        hi = (
            -42.379
            + 2.04901523 * t
            + 10.14333127 * rh
            - 0.22475541 * t * rh
            - 0.00683783 * t * t
            - 0.05481717 * rh * rh
            + 0.00122874 * t * t * rh
            + 0.00085282 * t * rh * rh
            - 0.00000199 * t * t * rh * rh
        )
        if rh < 13 and 80 < t < 112:
            hi -= ((13 - rh) / 4) * ((17 - abs(t - 95)) / 17) ** 0.5
        if rh > 85 and 80 < t < 87:
            hi += ((rh - 85) / 10) * ((87 - t) / 5)
    return hi


if __name__ == "__main__":
    for temp in [90, 100, 110]:
        print(f"=== {temp}°F ===")
        for rh in range(0, 101, 5):
            hi = heat_index(temp, rh)
            diff = hi - temp
            marker = " <-- FEELS COOLER" if hi < temp else ""
            print(f"  {rh:3d}% RH -> HI {hi:5.0f}°F  (diff {diff:+.0f}){marker}")
        print()

    print("=== Phoenix vs Miami ===")
    print(f"Phoenix: 110°F, 10% RH -> HI {heat_index(110, 10):.0f}°F (feels {heat_index(110, 10) - 110:+.0f})")
    print(f"Phoenix: 115°F,  5% RH -> HI {heat_index(115, 5):.0f}°F (feels {heat_index(115, 5) - 115:+.0f})")
    print(f"Miami:    90°F, 70% RH -> HI {heat_index(90, 70):.0f}°F (feels {heat_index(90, 70) - 90:+.0f})")
    print(f"Miami:    85°F, 85% RH -> HI {heat_index(85, 85):.0f}°F (feels {heat_index(85, 85) - 85:+.0f})")
