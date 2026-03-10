from dataclasses import dataclass
from typing import ClassVar

from .LarnitechDevice import LarnitechDevice


@dataclass(frozen=True, init=False)
class LarnitechDoorSensor(LarnitechDevice):
    entity_type: ClassVar[str] = "binary_sensor"

    def _setup_(self) -> None:
        super()._setup_()
        self.config.update(
            {
                "device_class": "door",
                "payload_on": "on",
                "payload_off": "off",
            }
        )

    def notify_ha(self) -> dict[str, str]:
        state = self.status.get("state")

        is_open = state in (1, "1", True, "true", "open", "opened")
        return {
            "state_topic": self.config["payload_on" if is_open else "payload_off"]
        }


__all__ = ["LarnitechDoorSensor"]
