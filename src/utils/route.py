class Route:
    def __init__(self, route: str):
        self._parts = [part for part in route.split("/") if part]

    @property
    def parts(self) -> list[str]:
        return self._parts

    @property
    def group(self) -> str | None:
        return self._parts[0] if len(self._parts) > 0 else None

    @property
    def control(self) -> str | None:
        return self._parts[1] if len(self._parts) > 1 else None
