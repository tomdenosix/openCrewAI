"""Telemetry configuration constants.

This module defines constants used for CrewAI telemetry configuration.
"""

from typing import Final


CREWAI_TELEMETRY_BASE_URL: Final[str] = "http://localhost:4318"
CREWAI_TELEMETRY_SERVICE_NAME: Final[str] = "crewAI-telemetry"

TRACER_NAME: Final[str] = "crewai.telemetry"
