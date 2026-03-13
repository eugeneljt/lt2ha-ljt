from .LarnitechDevice import LarnitechDevice

class LarnitechIntercom(LarnitechDevice):
    entity_type = "binary_sensor"

    def _setup_(self) -> None:
        self.config.update({
            "state_topic": "",
            "payload_on": "ON",
            "payload_off": "OFF",
            "icon": "mdi:doorbell",
        })

    def notify_ha(self) -> dict[str, str]:
        state = self.status.get("state")
        if not state:
            return {}
        is_ringing = int(state[0]) == 2
        return {
            "state_topic": "ON" if is_ringing else "OFF",
        }
