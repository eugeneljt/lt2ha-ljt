from .LarnitechDevice import LarnitechDevice
import logging

_LOGGER = logging.getLogger(__name__)


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
        _LOGGER.warning("INTERCOM raw state addr=%s state=%r status=%r", self.addr, state, self.status)

        is_ringing = self._is_ringing(state)

        return {
            "state_topic": "ON" if is_ringing else "OFF",
        }

    @staticmethod
    def _is_ringing(state) -> bool:
        if state is None:
            return False

        if isinstance(state, (int, float)):
            return int(state) == 2

        if isinstance(state, str):
            value = state.strip().lower()
            if value in {"2", "call", "calling", "ring", "ringing"}:
                return True
            if value in {"0", "1", "idle", "answer", "answered", "off", "false", "no_call", "no-call"}:
                return False
            return False

        if isinstance(state, (list, tuple)) and state:
            first = state[0]
            if isinstance(first, (int, float)):
                return int(first) == 2
            if isinstance(first, str):
                value = first.strip().lower()
                return value in {"2", "call", "calling", "ring", "ringing"}

        return False
