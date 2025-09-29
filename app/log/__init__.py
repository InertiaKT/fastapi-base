import logging
from app.log.trace_id import TRACE_ID_VAR, TraceIdFilter
from app.log.config import LogSettings

log_settings = LogSettings()

logging.basicConfig(
    level=log_settings.logging_level,
    format="%(asctime)s [%(levelname)s] [%(trace_id)s] %(name)s: %(message)s",
)

for handler in logging.getLogger().handlers:
    handler.addFilter(TraceIdFilter())

__all__ = ["TRACE_ID_VAR"]
